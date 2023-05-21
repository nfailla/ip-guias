
def alguno_es_0(numero1:float,numero2:float) -> bool:
  return numero1 == 0 or numero2 == 0

def ambos_son_0(numero1:float,numero2:float) -> bool:
  return numero1 == 0 and numero2 == 0

def es_nombre_largo(nombre: str) -> bool:
  length: int = len(nombre)
  return length >= 3 and length <= 8

def es_bisiesto(anio: int) -> bool:
  return es_multiplo_de(anio, 400) or (es_multiplo_de(anio, 4) and not es_multiplo_de(anio, 100))

def es_multiplo_de(n: int, m: int) -> bool:
  return n % m == 0