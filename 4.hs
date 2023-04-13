-- Ejercicio 4. ⋆
-- Especificar e implementar las siguientes funciones utilizando tuplas para representar pares, ternas de números.
--    a) prodInt: calcula el producto interno entre dos tuplas R × R.
prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt u v = fst u * fst v + snd u * snd v

--    b) todoMenor: dadas dos tuplas R×R, decide si es cierto que cada coordenada de la primera tupla es menor a la coordenada
--       correspondiente de la segunda tupla.
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor u v = (fst u < fst v) && (snd u < snd v)

--    c) distanciaPuntos: calcula la distancia entre dos puntos de R2.
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos a b = sqrt ((fst b - fst a) ^ 2 + (snd b - snd a) ^ 2)

--    d) sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.
--    e) sumarSoloMultiplos: dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que
--       son múltiplos del número natural. Por ejemplo:
--       sumarSoloMultiplos (10,-8,-5) 2 ⇝ 2
--       sumarSoloMultiplos (66,21,4) 5 ⇝ 0
--       sumarSoloMultiplos (-30,2,12) 3 ⇝ -18
--    f) posPrimerPar: dada una terna de enteros, devuelve la posición del primer número par si es que hay alguno, y devuelve
--       4 si son todos impares.
--    g) crearPar :: a ->b ->(a, b): crea un par a partir de sus dos componentes dadas por separado (debe funcionar para
--       elementos de cualquier tipo).
--    h) invertir :: (a, b) ->(b, a): invierte los elementos del par pasado como parámetro (debe funcionar para elementos
--       de cualquier tipo).