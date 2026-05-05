module Dice (rollDice) where

import System.Random (randomRIO)

rollDice :: Int -> Int -> IO [Int]
rollDice n sides = mapM (\_ -> randomRIO (1, sides)) [1..n]
