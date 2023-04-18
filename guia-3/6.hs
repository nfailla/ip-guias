-- Ejercicio 6. Programar una función bisiesto :: Integer ->Bool
--  pred EsMultiplo(x : Z, y : Z){x mod y = 0}
--  problema bisiesto (año: Z) : Bool {
--    requiere: {True}
--      asegura: {res = false ↔ (¬EsMultiplo(año, 4) ∨ (EsMultiplo(año, 100) ∧ ¬EsMultiplo(año, 400)))}
--    }
-- Por ejemplo:
-- bisiesto 1901 ⇝ False, bisiesto 1904 ⇝ True,
-- bisiesto 1900 ⇝ False, bisiesto 2000 ⇝ True.
bisiesto :: Integer -> Bool
-- bisiesto anio = not (not (esMultiplo anio 4) || (esMultiplo anio 100 && not (esMultiplo anio 400)))
-- De Morgan:
-- bisiesto anio = esMultiplo anio 4 && not (esMultiplo anio 100 && not (esMultiplo anio 400))
-- De Morgan:
bisiesto anio = esMultiplo anio 4 && (not (esMultiplo anio 100) || esMultiplo anio 400)

esMultiplo :: Integer -> Integer -> Bool
esMultiplo x y = (x `mod` y) == 0
