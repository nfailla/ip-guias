-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (prod (x :: (Integer)))

prod :: Integer -> Integer
-- Completar la definición de la función
prod n = prodAux (2 * n)

-- Pueden agregan las funciones que consideren necesarias
prodAux :: Integer -> Integer
prodAux 1 = (1 ^ 2) + (2 * 1)
prodAux i = ((i ^ 2) + (2 * i)) * prodAux (i - 1)
