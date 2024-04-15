problemafibonacci :: Int -> Int
problemafibonacci 0 = 0
problemafibonacci 1 = 1
problemafibonacci x = problemafibonacci(x-1)+ problemafibonacci(x-2)

parteEntera :: Float -> Int
parteEntera x | x>=0 = truncate x
              | x<0 = truncate (-x) 

esDivisible :: Int -> Int -> Bool
esDivisible x y | x-y==0 = True
                | (0 < x-y) && (x-y < y) = False
                | x-y >= y = esDivisible(x-y)(y)

sumaImpares :: Int -> Int
sumaImpares 1 = 1
sumaImpares x = sumaImpares(x-1) + (x*2-1)

medioFact :: Int -> Int
medioFact 0 = 1
medioFact 1 = 1
medioFact 2 = 2
medioFact x| x>2 = x * medioFact(x-2)

sumaDigitos :: Int -> Int
sumaDigitos x | x<=9 = x
              | otherwise = (sumaDigitos(div x 10)) + (mod x 10)

todosDigitosIguales :: Int -> Bool
todosDigitosIguales x | x<=9 = True
                      | 
                      | otherwise = False