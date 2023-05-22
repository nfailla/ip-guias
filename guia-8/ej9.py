def tiene_al_menos_tres_vocales_distintas (palabra: str) -> bool:
  vocales: list[str] = ["a", "e", "i", "o", "u"]
  cantidad_apariciones_diferentes: int = 0
  for i in range(0, vocales):
    cantidad_apariciones_vocal: int = palabra.lower().count(vocales[i])
    cantidad_apariciones_diferentes += min(1, cantidad_apariciones_vocal)
  
  return cantidad_apariciones_diferentes