-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Int, Int, Int)))

sumaMenosQueMax :: (Int, Int, Int) -> Bool
-- Completar acá la definición de la función
sumaMenosQueMax (a, b, c) = maximo a b c > minimo a b c + medio a b c

-- Pueden agregan las funciones que consideren necesarias
maximo :: Int -> Int -> Int -> Int
maximo a b c = max (max a b) c

minimo :: Int -> Int -> Int -> Int
minimo a b c = min (min a b) c

medio :: Int -> Int -> Int -> Int
medio a b c
  | a == b && b == elMinimo = a
  | a == c && c == elMinimo = a
  | b == c && c == elMinimo = b
  | a > elMinimo && a < elMaximo = a
  | b > elMinimo && b < elMaximo = b
  | otherwise = c
  where
    elMinimo = minimo a b c
    elMaximo = maximo a b c