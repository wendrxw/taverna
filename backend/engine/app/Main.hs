{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DeriveGeneric #-}

module Main where

import Network.Wai
import Network.Wai.Handler.Warp (run)
import Network.HTTP.Types
import Data.Aeson
import GHC.Generics (Generic)
import qualified Data.ByteString.Lazy as BL

import Dice
import Parser

-- =====================================================
-- 🎯 LEGACY DICE API
-- =====================================================

data RollRequest = RollRequest
  { expression :: String
  } deriving (Show, Generic)

instance FromJSON RollRequest

data RollResponse = RollResponse
  { rrResult    :: Int
  , rrRolls     :: [Int]
  , rrModifier  :: Int
  , rrBreakdown :: [String]
  } deriving (Show, Generic)

instance ToJSON RollResponse

-- =====================================================
-- ⚔️ COMBAT ENGINE TYPES
-- =====================================================

data ActionType
  = Attack
  | Damage
  | SkillCheck
  | SavingThrow
  deriving (Show, Generic)

instance ToJSON ActionType

data ActionRequest = ActionRequest
  { actionReq   :: String
  , modReq      :: Int
  , targetACReq :: Maybe Int
  , diceReq     :: Maybe Int
  , sidesReq    :: Maybe Int
  } deriving (Show, Generic)

instance FromJSON ActionRequest

data DiceRoll = DiceRoll
  { drRolls    :: [Int]
  , drModifier :: Int
  , drTotal    :: Int
  } deriving (Show, Generic)

instance ToJSON DiceRoll

data ActionResponse = ActionResponse
  { arActionType :: ActionType
  , arResult     :: Int
  , arSuccess    :: Maybe Bool
  , arHit        :: Maybe Bool
  , arCritical   :: Bool
  , arRolls      :: [Int]
  , arModifier   :: Int
  , arBreakdown  :: [String]
  } deriving (Show, Generic)

instance ToJSON ActionResponse

-- =====================================================
-- 🚀 MAIN
-- =====================================================

main :: IO ()
main = do
    putStrLn "⚔️ RPG Combat Engine running on port 8080"
    run 8080 app

-- =====================================================
-- 🧠 ENGINE CORE
-- =====================================================

safeHead :: [a] -> Maybe a
safeHead (x:_) = Just x
safeHead []    = Nothing

app :: Application
app req respond =
    case (requestMethod req, pathInfo req) of

        -- 🎲 LEGACY DICE (compatível)
        ("POST", ["engine", "roll"]) -> do
            body <- strictRequestBody req

            case decode body :: Maybe RollRequest of
                Just reqBody ->
                    case parseDice (expression reqBody) of
                        Just (n, sides, modif) -> do

                            rolls <- rollDice n sides

                            let base = sum rolls
                            let total = base + modif

                            let breakdown =
                                  [ "🎲 Expression: " ++ expression reqBody
                                  , "🎯 Rolls: " ++ show rolls
                                  , "➕ Base: " ++ show base
                                  , "⚙️ Modifier: " ++ show modif
                                  , "🧮 Total: " ++ show total
                                  ]

                            respond $
                                responseLBS status200 jsonHeader $
                                encode $ RollResponse total rolls modif breakdown

                        Nothing ->
                            badRequest respond "Invalid dice expression"

                Nothing ->
                    badRequest respond "Invalid JSON body"

        -- ⚔️ COMBAT ENGINE
        ("POST", ["engine", "action"]) -> do
            body <- strictRequestBody req

            case decode body :: Maybe ActionRequest of
                Just reqBody -> do

                    case actionReq reqBody of

                        -- =========================
                        -- ⚔️ ATTACK
                        -- =========================
                        "attack" -> do

                            attackRoll <- rollDice 1 20

                            case safeHead attackRoll of
                                Nothing ->
                                    badRequest respond "Dice engine failed"

                                Just nat -> do

                                    let modif = modReq reqBody
                                    let ac = maybe 10 id (targetACReq reqBody)

                                    let total = nat + modif

                                    let isCrit = nat == 20
                                    let isHit  = nat == 20 || total >= ac

                                    let dmgBase =
                                          if not isHit
                                          then 0
                                          else if isCrit
                                               then 12
                                               else 6

                                    let finalDamage =
                                          if isHit
                                          then dmgBase + modif
                                          else 0

                                    let breakdown =
                                          [ "⚔️ Roll: " ++ show nat
                                          , "➕ Mod: " ++ show modif
                                          , "🛡 AC: " ++ show ac
                                          , "💥 Hit: " ++ show isHit
                                          , "🔥 Crit: " ++ show isCrit
                                          , "⚔️ Damage: " ++ show finalDamage
                                          ]

                                    respond $
                                        responseLBS status200 jsonHeader $
                                        encode $ ActionResponse
                                            Attack
                                            finalDamage
                                            Nothing
                                            (Just isHit)
                                            isCrit
                                            attackRoll
                                            modif
                                            breakdown

                        -- =========================
                        -- 🧠 SKILL
                        -- =========================
                        "skill" -> do

                            roll <- rollDice 1 20

                            case safeHead roll of
                                Nothing ->
                                    badRequest respond "Dice engine failed"

                                Just nat -> do

                                    let modif = modReq reqBody
                                    let dc = maybe 10 id (targetACReq reqBody)

                                    let total = nat + modif
                                    let success = total >= dc

                                    let breakdown =
                                          [ "🧠 Roll: " ++ show nat
                                          , "➕ Mod: " ++ show modif
                                          , "📊 DC: " ++ show dc
                                          , "✔ Success: " ++ show success
                                          ]

                                    respond $
                                        responseLBS status200 jsonHeader $
                                        encode $ ActionResponse
                                            SkillCheck
                                            total
                                            (Just success)
                                            Nothing
                                            False
                                            roll
                                            modif
                                            breakdown

                        -- =========================
                        -- 💥 DAMAGE
                        -- =========================
                        "damage" -> do

                            let diceN = maybe 1 id (diceReq reqBody)
                            let sidesN = maybe 6 id (sidesReq reqBody)

                            rolls <- rollDice diceN sidesN

                            let total = sum rolls + modReq reqBody

                            let breakdown =
                                  [ "💥 Rolls: " ++ show rolls
                                  , "🧮 Total: " ++ show total
                                  ]

                            respond $
                                responseLBS status200 jsonHeader $
                                encode $ ActionResponse
                                    Damage
                                    total
                                    Nothing
                                    Nothing
                                    False
                                    rolls
                                    (modReq reqBody)
                                    breakdown

                        _ ->
                            badRequest respond "Unknown action"

                Nothing ->
                    badRequest respond "Invalid JSON body"

        -- ❤️ HEALTH
        ("GET", ["health"]) ->
            respond $
                responseLBS status200 jsonHeader $
                encode $ object ["status" .= ("ok" :: String)]

        -- ❌ NOT FOUND
        _ ->
            respond $
                responseLBS status404 jsonHeader $
                encode $ object ["error" .= ("Not found" :: String)]

-- =====================================================
-- 🔧 HELPERS
-- =====================================================

jsonHeader :: ResponseHeaders
jsonHeader =
    [("Content-Type", "application/json")]

badRequest :: (Response -> IO ResponseReceived) -> String -> IO ResponseReceived
badRequest respond msg =
    respond $
        responseLBS status400 jsonHeader $
        encode $ object ["error" .= msg]