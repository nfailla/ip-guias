-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (sumaDigitos (x :: (Int)))

sumaDigitos :: Int -> Int
-- Completar la definición de la función
sumaDigitos n
  | n < 10 = n
  | otherwise = ultimoDigito n + sumaDigitos (sinUltimoDigito n)

-- Pueden agregan las funciones que consideren necesarias
ultimoDigito :: Int -> Int
ultimoDigito n = n `mod` 10

sinUltimoDigito :: Int -> Int
sinUltimoDigito n = n `div` 10
