-- Ejercicio 8. Implementar una función comparar :: Integer ->Integer ->Integer
--  problema comparar (a:Z, b:Z) : Z {
--    requiere: {T rue}
--    asegura: {(res = 1 ↔ sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
--    asegura: {(res = −1 ↔ sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
--    asegura: {(res = 0 ↔ sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b)))}
--  }

--  problema sumaUltimosDosDigitos (x: Z) : Z {
--    requiere: {T rue}
--    asegura: {res = (x mod 10) + (⌊(x/10)⌋ mod 10)}
--  }

-- Por ejemplo:
-- comparar 45 312 ⇝ -1 porque 312 ≺ 45 y 1 + 2 < 4 + 5.
-- comparar 2312 7 ⇝ 1 porque 2312 ≺ 7 y 1 + 2 < 0 + 7.
-- comparar 45 172 ⇝ 0 porque no vale 45 ≺ 172 ni tampoco 172 ≺ 45.

comparar :: Integer -> Integer -> Integer
comparar a b
  | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
  | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
  | otherwise = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = (x `mod` 10) + ((x `div` 10) `mod` 10)