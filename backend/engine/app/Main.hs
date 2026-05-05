{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DeriveGeneric #-}

module Main where

import Network.Wai
import Network.Wai.Handler.Warp (run)
import Network.HTTP.Types
import Data.Aeson
import GHC.Generics (Generic)
import Dice
import Parser

-- 🔷 Tipos

data RollRequest = RollRequest
  { expression :: String
  } deriving (Show, Generic)

instance FromJSON RollRequest

data RollResponse = RollResponse
  { result :: Int
  , rolls :: [Int]
  , modifier :: Int
  } deriving (Show, Generic)

instance ToJSON RollResponse

-- 🔷 Main

main :: IO ()
main = do
    putStrLn "Dice Engine running on port 8080"
    run 8080 app

-- 🔷 App

app :: Application
app req respond =
    case (requestMethod req, pathInfo req) of

        ("POST", ["engine", "roll"]) -> do
            body <- strictRequestBody req

            case decode body :: Maybe RollRequest of
                Just reqBody ->
                    case parseDice (expression reqBody) of
                        Just (n, sides, modif) -> do
                            rolls <- rollDice n sides
                            let total = sum rolls + modif

                            respond $ responseLBS
                                status200
                                jsonHeader
                                (encode $ RollResponse total rolls modif)

                        Nothing ->
                            badRequest "Invalid dice expression"

                Nothing ->
                    badRequest respond "Invalid JSON body"

        ("GET", ["health"]) ->
            respond $ responseLBS
                status200
                jsonHeader
                (encode $ object ["status" .= ("ok" :: String)])

        _ ->
            respond $ responseLBS
                status404
                jsonHeader
                (encode $ object ["error" .= ("Not found" :: String)])

-- 🔷 Helpers

jsonHeader :: ResponseHeaders
jsonHeader = [("Content-Type", "application/json")]

badRequest :: (Response -> IO ResponseReceived) -> String -> IO ResponseReceived
badRequest respond msg =
    respond $ responseLBS
        status400
        jsonHeader
        (encode $ object ["error" .= msg])