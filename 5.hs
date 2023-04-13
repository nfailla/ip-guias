-- Ejercicio 5. Implementar la función todosMenores :: (Integer, Integer, Integer) -> Bool
--    problema todosMenores ((n1,n2,n3) : Z × Z × Z) : Bool {
--      requiere: {True}
--      asegura: {(res = true) ↔ ((f(n1) > g(n1)) ∧ (f(n2) > g(n2)) ∧ (f(n3) > g(n3))))}
--    }
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) = (f n1 > g n1) && (f n2 > g n2) && (f n3 > g n3)

--    problema f (n: Z) : Z {
--      requiere: {True}
--      asegura: {(n ≤ 7 → res = n^2) ∧ (n > 7 → res = 2n − 1)}
--    }
f :: Integer -> Integer
f n
  | n <= 7 = n ^ 2
  | otherwise = 2 * n - 1

--    problema g (n: Z) : Z {
--      requiere: {True}
--      asegura: {res = if esPar(n) then n/2 else 3n + 1 fi}
--    }
g :: Integer -> Integer
g n = if esPar n then n `div` 2 else 3 * n + 1

--    pred esPar(n : Z){ (n mod 2) = 0 }
esPar :: Integer -> Bool
esPar n = (n `mod` 2) == 0