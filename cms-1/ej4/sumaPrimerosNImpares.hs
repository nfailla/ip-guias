-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (sumaPrimerosNImpares (x :: (Integer)))

sumaPrimerosNImpares :: Integer -> Integer
-- Completar la definición de la función
-- sumaPrimerosNImpares 1 = 0
-- sumaPrimerosNImpares n = sumaPrimerosNImparesAux (2 * n) - 1
sumaPrimerosNImpares 1 = 0
sumaPrimerosNImpares n
  | hasta < 1 = 0
  | otherwise = sumaPrimerosNImparesAux hasta
  where
    hasta = (2 * n) - 1

-- Pueden agregan las funciones que consideren necesarias

sumaPrimerosNImparesAux :: Integer -> Integer
sumaPrimerosNImparesAux 1 = 2 * 1 + 2
sumaPrimerosNImparesAux i
  | esPar i = 0
  | otherwise = ((2 * i) + 2) + sumaPrimerosNImparesAux (i - 1)

esPar :: Integer -> Bool
esPar a = a `mod` 2 == 0