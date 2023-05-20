def del_1_al_10 () -> None:
  n = 1
  while n <= 10:
    print(n)
    n += 1

def pares_entre_10_y_40 () -> None:
  n = 10
  while n <= 40:
    if n % 2 == 0:
      print(n)
    n += 1

def eco () -> None:
  i = 0
  while i < 10:
    print("eco")
    i += 1

def cuenta_regresiva (ordinal: int) -> None:
  while ordinal > 1:
    print(ordinal)
    ordinal -= 1
  print("Despegue")

def monitorear_viaje_en_el_tiempo (anio_de_partida: int, algun_anio_de_llegada: int) -> None:
  anio_actual = anio_de_partida
  while anio_actual > algun_anio_de_llegada:
    print("Viajó un año al pasado, estamos en el año: " + anio_actual)
    anio_actual -= 1


def monitorear_viaje_en_el_tiempo_hasta_aristoteles (anio_de_partida: int) -> None:
  anio_actual = anio_de_partida
  anio_aristotelico = -384
  while anio_actual > anio_aristotelico:
    print("Viajó 20 años al pasado, estamos en el año: " + anio_actual)
    anio_actual -= 20

