from math import sqrt

def raizDe2() -> float:
  return round(sqrt(2), 4)

def imprimir_hola() -> None:
  print("hola")

def imprimir_un_verso() -> None:
  print("Fui a Vandalucía") 
  print("Donde su pueblo está")
  print("No tardé en sentirme")
  print("Un luchador total")

def factorial_de_dos() -> int:
  return factorial_de(2)

def factorial_de_tres() -> int:
  return factorial_de(3)

def factorial_de_cuatro() -> int:
  return factorial_de(4)

def factorial_de_cinco() -> int:
  return factorial_de(5)


def factorial_de(n: int) -> int:
  res: int = 1
  for i in range(1, n):
    res *= i
  return res

