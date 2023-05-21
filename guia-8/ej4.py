from typing import List

def ordenados (s: List[int]) -> bool:
  resultado: bool = True
  for i in range(0, len(s) - 1):
    if not s[i] < s[i + 1]:
      resultado = False
  
  return resultado