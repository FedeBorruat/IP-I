relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = False
relacionesValidas ((x,y):xs) | not (repetido ((x,y):xs)) = False
                             | contenido (x,y) xs || contenido (y,x) xs = False
                             | otherwise = True

contenido :: (Eq  t) => (t,t) -> [(t,t)] -> Bool
contenido _ [] = False
contenido x (y:xs) | fst x == fst y && snd x == snd y  = True
                   | otherwise = contenido x xs 
                   
repetido :: Eq a => [(a, a)] -> Bool
repetido [] = True
repetido ((a):xs) | fst a==snd a = False
                  | otherwise = repetido xs

--personas :: [(String, String)] -> [String]
--personas [] = ["nadie"]


--amigosDe :: String -> [(String, String)] -> [String]
--amigosDe "nadie" [] = ["nadie"]
-- esta mal. lo tenes que corregir

--personaConMasAmigos :: [(String, String)] -> String
--personaConMasAmigos [] = "yo"