-- Ejercicio 7. Implementar una función:
--  distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) ->Float
--  problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
--  requiere: {True}
--  asegura: {res = sumatoria<i=0; 2; |p[i] - q[i]|>
--  }
--  Por ejemplo:
--  distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9
--  distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (vx, vy, vz) (wx, wy, wz) = abs ((vx - wx) + (vy - wy) + (vz - wz))