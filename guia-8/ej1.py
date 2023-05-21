from typing import List

def pertenece (s: List[int], e: int) -> bool:
  i: int = 0
  encontrado: bool = False
  while i < len(s) or encontrado:
    i += 1
    if s[i] == e:
      encontrado = True
