--Guia Practica 4--
--Problema1--
problemafibonacci :: Int -> Int
problemafibonacci 0 = 0
problemafibonacci 1 = 1
problemafibonacci x = problemafibonacci(x-1)+ problemafibonacci(x-2)
--Problema2--
parteEntera :: Float -> Int
parteEntera x | x>=0 = truncate x
              | x<0 = truncate (-x) 
--Problema3--
esDivisible :: Int -> Int -> Bool
esDivisible x y | x-y==0 = True
                | (0 < x-y) && (x-y < y) = False
                | x-y >= y = esDivisible(x-y)(y)
--Problema4--
sumaImpares :: Int -> Int
sumaImpares 1 = 1
sumaImpares x = sumaImpares(x-1) + (x*2-1)
--Problema5--
medioFact :: Int -> Int
medioFact 0 = 1
medioFact 1 = 1
medioFact 2 = 2
medioFact x| x>2 = x * medioFact(x-2)
--Problema6--
sumaDigitos :: Int -> Int
sumaDigitos x | x<=9 = x
              | otherwise = (sumaDigitos(div x 10)) + (mod x 10)
--Problema7--
todosDigitosIguales :: Int -> Bool
todosDigitosIguales x | mod x 10 == div ((mod x 100) - (mod x 10)) 10 = todosDigitosIguales(div (x -(mod x 10)) 10)
                      | x<=9 = True
                      | otherwise = False
--Problema8-- 
iesimoDigito :: Int -> Int -> Int
iesimoDigito x i = div (mod x (10^i)) (10^(i-1))
--Problema9--
esCapicua :: Int -> Bool
esCapicua x | x<=9 = True
            | ultimoDigito x == digitoUnidad x = esCapicua(div ((x - digitoUnidad(x)) - (ultimoDigito x * 10^((numerosDigitos x)-1))) 10)
            | otherwise = False
digitoUnidad :: Int -> Int 
digitoUnidad x | 0<x = mod x 10
               | otherwise = mod (-x) 10
numerosDigitos :: Int -> Int
numerosDigitos 0=0
numerosDigitos x | x<=9 =1
                 | otherwise = 1 + numerosDigitos(div x 10)
ultimoDigito :: Int -> Int
ultimoDigito x | x<=9 = x
               | otherwise = ultimoDigito (div x 10) 
--Problema10--
--a--
--requiere: True
--asegura: res= sumatoria de 2^n desde 0 hasta n
f1 :: Int -> Int
f1 x | x==0 = 1
     | x>0 = 2^x + (f1 (x-1))
--b--
--requiere: True
--asegura: res= sumatoria de q^n desde 1 hasta n
f2 :: Int -> Float -> Float
f2 _ 0 = 0
f2 0 _ = 0
f2 n q = q^n + f2(n-1)(q)
--c--
--requiere: n<=1
--asegura: res= sumatoria de q^n desde 1 hasta 2n
f3 :: Int -> Float -> Float
f3 n q | q==1 = fromIntegral(n+n)
       | n==1 = q + q^2
       | otherwise = q^(n+n) + f2(n+n-1)(q)
--d--
--requiere: True
--asegura: res= sumatoria de q^n desde n hasta 2n
f4 :: Int -> Float -> Float
f4 n q | n==0 = 1
       | otherwise =  f3(n)(q)- f2 (n-1)(q)
--Problema11--
--a--
eAprox :: Int -> Float
eAprox x = eAprox1(fromIntegral x)
eAprox1 :: Float -> Float
eAprox1 0=1
eAprox1 x = (1/(factor(x)) + eAprox1(x-1))
factor :: Float -> Float
factor x| x==0 = 1
factor x = x* (factor(x-1))
--b--
e :: Float
e = (eAprox1 1 + eAprox1 2 +eAprox1 3 +eAprox1 4 +eAprox1 5+eAprox1 6 + eAprox1 7 +eAprox1 8 +eAprox1 9 +eAprox1 10)/10
--Problema12--
raizDe2Aprox :: Int -> Float
raizDe2Aprox x = aa x 2 
aa :: Int -> Float -> Float
aa l y | l==1 = y-1
       | l>1 = aa (l-1) (2 + (1/y))
--Problema13--
sumsum :: Int -> Int -> Int
sumsum n m | n==1 = m
           | m==1 = sumatoria n 1
           | otherwise = (sumatoria(n)(m)) + (sumsum (n)(m-1))
sumatoria :: Int -> Int -> Int
sumatoria x y | x==0 = 0
sumatoria x y | x==1 = x
              | otherwise = x^y + sumatoria(x-1)(y)
--Problema16--
--a--
menorDivisor :: Int -> Int
menorDivisor x = md1 x 2
md1 :: Int -> Int -> Int
md1 x y| mod x y == 0 = y
       | mod x y /= 0 = md1(x)(y+1)
       | y==x = 0
--b--
esPrimo :: Int -> Bool
esPrimo x | x== (menorDivisor x) = True
          | otherwise = False
--c--
sonCoprimos :: Int -> Int -> Bool
sonCoprimos x y = esPrimo x == True && esPrimo y == True
--d--
nEsimoPrimo :: Int -> Int 
nEsimoPrimo x = nep 2 1 x
nep :: Int -> Int -> Int -> Int
nep n cp 0 = 0
nep n cp ep | (esPrimo n == True)&&(cp==ep) = n 
            | (esPrimo n == True)&&(cp/=ep) = nep (n+1) (cp+1) ep  
            |  esPrimo n == False = nep (n+1) cp ep
--Problema19--
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos x = esSumaInicialDePrimos1 x 1 2

esSumaInicialDePrimos1 :: Int -> Int -> Int -> Bool
esSumaInicialDePrimos1 x np sdp  | x==sdp = True
                                 | x<(sdp) = False
                                 | x>(sdp) = esSumaInicialDePrimos1 x (np+1) (sdp+(nEsimoPrimo(np+1)))
