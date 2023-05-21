from typing import List

def alguna_mayor_a_7 (palabras: List[str]) -> bool:
  resultado: bool = False
  i: int = 0
  while not resultado and i < len(palabras):
    i += 1
    if len(palabras[i]) > 7:
      resultado = True
  return resultado
