-- Ejercicio 9. A partir de las siguientes implementaciones en Haskell, describir en lenguaje natural qué hacen y especificarlas
-- semiformalmente.
-- a) f1 :: Float => Float
--    f1 n | n == 0 = 1
--         | otherwise = 0

-- Toma un nro real, y devuelve 1 en caso de ser cero. Devuelve 0 en caso contrario.
-- problema f1 (n: R): R {
--   requiere: { True }
--   asegura: { (n = 0 => res = 1) ^ (n /= 0 => res = 0) }
-- }

-- b) f2 :: Float => Float
--    f2 n | n == 1 = 15
--         | n == -1 = -15

-- Toma un nro real igual a 1 ó -1, y devuelve 15 para el primer caso, o -15 para el segundo
-- problema f2 (n: R): R {
--   requiere: { n = 1 v n = -1 }
--   asegura: { (n = 1 => res = 15) ^ (n = -1 => res = -15) }
-- }

-- c) f3 :: Float => Float
--    f3 n | n <= 9 = 7
--         | n >= 3 = 5

-- Toma un nro real, y devuelve 7 si dicho nro es menor o igual a 9, ó 5 si dicho nro es mayor a 9.
-- problema f3 (n: R): R {
--   requiere: { True }
--   asegura: { (n <= 9 => res = 7) ^ (n > 9 => res = 5) }
-- }

-- d) f4 :: Float => Float => Float
--    f4 x y = (x + y) / 2
-- Toma dos nros reales, y devuelve la mitad de la suma de ambos.
-- problema f4 (x: R, y: R): R {
--   requiere: { True }
--   asegura: { res = ((x + y) / 2) }
-- }

-- e) f5 :: (Float, Float) => Float
--    f5 (x, y) = (x + y) / 2
-- Toma una tupla 'a' perteneciente a RxR y devuelve la mitad de la suma de sus dos componentes
-- problema f5 (a: RxR): R {
--   requiere: { True }
--   asegura: { res = ((a_0 + a_1) / 2) }
-- }

-- f) f6 :: Float => Int => Bool
-- f6 a b = truncate a == b
