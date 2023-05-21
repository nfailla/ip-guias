from typing import List

def divideATodos (s: List[int], e: int) -> bool:
  # for el in s: # se puede usar???
  resultado: bool = True
  for i in range(0, len(s)):
    if s[i] % e != 0:
      resultado = False
  
  return resultado