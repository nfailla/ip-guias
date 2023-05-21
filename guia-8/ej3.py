from typing import List

def sumaTotal (s: List[int]) -> bool:
  suma: int = 0
  for i in range(0, len(s)):
    suma += s[i]
  
  return suma