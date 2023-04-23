-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (combinacionesMenoresOiguales (x :: (Integer)))

combinacionesMenoresOiguales :: Integer -> Integer
-- Completar la definición de la función
combinacionesMenoresOiguales n = aux n n n

-- Pueden agregan las funciones que consideren necesarias
aux :: Integer -> Integer -> Integer -> Integer
aux n 1 1 = sumSiPred n 1 1
aux n 1 j = sumSiPred n 1 j + aux n n (j - 1)
aux n i j = sumSiPred n i j + aux n (i - 1) j

sumSiPred :: Integer -> Integer -> Integer -> Integer
sumSiPred n i j = if (i * j) <= n then 1 else 0