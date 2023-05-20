from math import ceil, sqrt


def imprimir_saludo(nombre: str) -> None:
  print ("Hola " + nombre)
  
def raiz_cuadrada_de(nro: int) -> float:
  return sqrt(nro)

def imprimir_dos_veces(estribillo: str) -> None:
  print(estribillo * 2)

def es_multiplo_de(n: int, m: int) -> bool:
  return n % m == 0

def es_par (nro: int) -> bool:
  return es_multiplo_de(nro, 2)

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int:
  porciones_suficientes = comensales * min_cant_de_porciones
  return ceil(porciones_suficientes / 8)
