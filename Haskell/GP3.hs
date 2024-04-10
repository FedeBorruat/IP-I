f1 :: Int -> Int
f1 n  | n==1 = 8
     | n==4 = 131
     | n==16 = 16

g1 :: Int -> Int
g1 n | n==8 = 16
    | n==16 = 4
    | n==131 = 1

h1 :: Int -> Int 
h1 n = f (g n) 

k1 :: Int -> Int
k1 n = g (f n)

absoluto :: Int -> Int
absoluto n | n>=0 = n
           | otherwise = (-n) 

maximoabsoluto :: Int -> Int -> Int
maximoabsoluto x y | (absoluto x) < (absoluto y) = (absoluto y)
                   | otherwise = (absoluto x)

maximo3 :: Int -> Int -> Int -> Int
maximo3 a b c| a<=b && b<=c = c
             | c<=b = b
             | b<=c && c<=a = a
             | a<=c = c
             | c<=a && a<=b = b
             | b<=a = a

algunoes0 ::  Float -> Float -> Bool
algunoes0 x y | x==0 = True
              | y==0 = True
              | otherwise = False
             
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y | x==0 && y==0 = True
              | otherwise = False

mismoIntervalo :: (Int,Int) -> Bool
mismoIntervalo (x,y) | (x,y)==(0,3) || (x,y)==(3,7) || (x,y)==(7,0) = True
                     | otherwise = False

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos a b c | a==b && b==c = 0
                    | c/=b && a==b = c
                    | b==c && a/=b = a
                    | b/=c && a==c = b
                    | otherwise = (a+b+c)

esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y ==0 = True
                 | otherwise = False

digitoUnidad :: Int -> Int 
digitoUnidad x | 0<x = mod x 10
               | otherwise = mod (-x) 10

digitoDecena :: Int -> Int
digitoDecena x | 0<x = div (mod x 100) 10 
               | otherwise = div (mod (-x) 100) 10

estanRelacionados :: Int -> Int -> Bool
estanRelacionados 0 0 = False
estanRelacionados 0 _ = True
estanRelacionados _ 0 = True
estanRelacionados x y | mod x y == 0 = True 



productoInterno :: (Float,Float) -> (Float,Float) -> Float
productoInterno (a,b) (c,d) = a*c + b*d

todoMenor :: (Int,Int) -> (Int,Int) -> Bool
todoMenor (a,b) (c,d) | a<c && b<d = True
                      | otherwise = False

distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt((a-c)^2 + (b-d)^2)

sumaTerna :: (Int,Int,Int) -> Int
sumaTerna (a,b,c) = a+b+c

posPrimerPar :: (Int,Int,Int) -> Int
posPrimerPar (a,b,c) | mod a 2 == 0 = 1
                     | mod b 2 == 0 = 2
                     | mod c 2 == 0 = 3
                     | otherwise = 4

crearPar :: Float -> Float -> (Float,Float)
crearPar a b = (a,b)

invertir :: Float -> Float -> (Float,Float)
invertir a b = (b,a)

todosMenores :: (Int,Int,Int) -> Bool
todosMenores (a,b,c) |  (f a) > (g a) && (f b) > (g b) && (f c) >(g c) = True
                    | otherwise = False

f :: Int -> Int
f x | x<=7 = x*x
f x | x>7 = 2*x-1

g :: Int -> Int
g x | mod x 2 == 0 = div x 2
    | otherwise = x*3+1

bisiesto :: Int -> Bool
bisiesto x | mod x 4 /= 0 = False
           | mod x 100 == 0 && mod x 400 /= 0 = False
           | otherwise = True

absoluto1 :: Float -> Float
absoluto1 n | n>=0 = n
      | otherwise = (-n) 

distMan :: (Float,Float,Float) -> (Float,Float,Float) -> (Float)
distMan (x,y,z) (d,e,f) = (absoluto1 (x-d)) + (absoluto1 (y-e)) + (absoluto1 (z-f))

comparar :: Int -> Int -> Int
comparar a b | (digitoDecena a + digitoUnidad a) < (digitoDecena b + digitoUnidad b) = 1
             | (digitoDecena a + digitoUnidad a) == (digitoDecena b + digitoUnidad b) = 0
             | (digitoDecena a + digitoUnidad a) > (digitoDecena b + digitoUnidad b) = -1
