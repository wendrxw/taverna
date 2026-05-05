module Parser (parseDice) where

import Data.Char (isDigit)

parseDice :: String -> Maybe (Int, Int, Int)
parseDice str =
    case span isDigit str of
        (nStr, 'd':rest) ->
            case span isDigit rest of
                (dStr, '+' : modStr) ->
                    Just (read nStr, read dStr, read modStr)
                (dStr, "") ->
                    Just (read nStr, read dStr, 0)
                _ -> Nothing
        _ -> Nothing
