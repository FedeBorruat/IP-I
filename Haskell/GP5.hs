--1.1--
longitud :: (Eq t) => [t] -> Int
longitud [] = l
longitud (x:xs) = (l+1) + longitud (xs)
l ::Int
l=0
--1.2--
ultimo :: (Eq t) => [t] -> t
ultimo (x:xs) | longitud (x:xs) == 1 = x
              | longitud (x:xs) > 1 = ultimo xs
--1.3--

--2.1--
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | x==n = True
                   | otherwise = pertenece n xs 
--2.4--
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x :xs) = pertenece x xs || hayRepetidos xs 
--2.5--
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) | x==n = xs
                | x/=n = x:quitar n xs
--3.3-- 
maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x>y = maximo (x:xs) 
                | otherwise = maximo (y:xs)
--3.9--
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:y:xs) | x > maximo (y:xs) = x: ordenar(y:xs)
                 | otherwise = ordenar(y:xs)++[x] 
