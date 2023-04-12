-- 1. Definición de funciones básicas
-- Ejercicio 1. a) Implentar la función parcial f :: Integer ->Integer definida por extensión de la siguiente manera:
--    f(1) = 8
--    f(4) = 131
--    f(16) = 16

-- cuya especificación es la siguiente:
--    problema f (n: Z) : Z {
--       requiere: {n = 1 ∨ n = 4 ∨ n = 16}
--       asegura: {(n = 1 → result = 8) ∧ (n = 4 → result = 131) ∧ (n = 16 → result = 16)}
--    }

-- b) Análogamente, especificar e implementar la función parcial g :: Integer ->Integer
--    g(8) = 16
--    g(16) = 4
--    g(131) = 1

-- c) A partir de las funciones definidas en los ítems 1 y 2, implementar las funciones parciales h = f ◦ g y k = g ◦ f

f :: Integer -> Integer
f n
  | n == 1 = 8
  | n == 4 = 131
  | n == 16 = 16

g :: Integer -> Integer
g n
  | n == 8 = 16
  | n == 16 = 4
  | n == 131 = 1

h :: Integer -> Integer
h n = f (g n) -- O bien usando el operador '.': h = f . g

k :: Integer -> Integer
k n = g (f n) -- O bien usando el operador '.': k = g . f
