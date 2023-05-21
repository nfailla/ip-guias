def del_1_al_10 () -> None:
  for n in range(0, 10):
    print(n+1)

def pares_entre_10_y_40 () -> None:
  for n in range(10, 41):
    if n % 2 == 0:
      print(n)

def eco () -> None:
  for _ in range(0, 10):
    print("eco")

def cuenta_regresiva (ordinal: int) -> None:
  for i in range(ordinal, 1, -1):
    print(i)
  print("Despegue")

def monitorear_viaje_en_el_tiempo (anio_de_partida: int, algun_anio_de_llegada: int) -> None:
  for anio_actual in range(anio_de_partida, algun_anio_de_llegada, -1):
    print("Viajó un año al pasado, estamos en el año: " + anio_actual)


def monitorear_viaje_en_el_tiempo_hasta_aristoteles (anio_de_partida: int) -> None:
  anio_aristotelico: int = -384
  for anio_actual in range(anio_de_partida, anio_aristotelico, -20):
    print("Viajó 20 años al pasado, estamos en el año: " + anio_actual)
