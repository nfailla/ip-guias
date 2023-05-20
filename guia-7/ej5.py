# problema devolver_el_doble_si_es_par (nro: Z): Z {
#   requiere: { True }
#   asegura:  { (nro `mod` 2 = 0 -> res = 2 * nro) && (nro `mod` 2 /= 0 -> res = nro) }
# }
def devolver_el_doble_si_es_par (nro: int) -> int:
  if nro % 2 == 0:
    return nro * 2
  else:
    return nro

# problema devolver_valor_si_es_par_sino_el_que_sigue (nro: Z): Z {
#   requiere: { True }
#   asegura:  { (nro `mod` 2 = 0 -> res = nro) && (nro `mod` 2 /= 0 -> res = nro + 1) }
# }
def devolver_valor_si_es_par_sino_el_que_sigue (nro: int) -> int:
  if nro % 2 == 0:
    return nro
  return nro + 1

# problema devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (nro: Z): Z {
#   requiere: { True }
#   asegura:  { (nro `mod` 9 = 0 -> res = nro * 3) }
#   asegura:  { (nro `mod` 3 = 0 -> res = nro * 2) }
#   asegura:  { ((nro `mod` 9 /= 0 && nro `mod` 3 /= 0) -> res = nro) }
# }
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (nro: int) -> int:
  if nro % 9 == 0:
    return nro * 3
  elif nro % 3 == 0:
    return nro * 2
  else:
    return nro

# problema analizar_nombre (nombre: seq<char>): seq<char> {
#   requiere: { True }
#   asegura:  { |nombre| >= 5 -> res = "Tu nombre tiene muchas letras!" }
#   asegura:  { |nombre| < 5  -> res = "Tu nombre tiene menos de 5 caracteres" }
# }
def analizar_nombre (nombre: str) -> str:
  if len(nombre) >= 5:
    return "Tu nombre tiene muchas letras!"
  return "Tu nombre tiene menos de 5 caracteres"

# problema analizar_nombre (sexo: seq<char>, edad: N_0): seq<char> {
#   requiere: { sexo pertenece a <"M", "F"> }
#   asegura:  { menor(edad) -> res = "Andá de vacaciones" }
#   asegura:  { jubilada(sexo, edad) -> res = "Andá de vacaciones" }
#   asegura:  { jubilado(sexo, edad) -> res = "Andá de vacaciones" }
#   asegura:  { ~menor(edad) && ~jubilada(sexo, edad) && ~jubilado(sexo, edad) -> res = "Te toca trabajar" }
# }
# pred menor (edad: N_0) {
#   edad < 18
#}
# pred jubilada (sexo: seq<char>, edad: N_0) {
#   sexo = "F" and edad >= 60
#}
# pred jubilado (sexo: seq<char>, edad: N_0) {
#   sexo = "M" and edad >= 65
#}
def cielo_o_infierno (sexo: str, edad: int) -> str:
  if (edad < 18) or (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65):
    return "Andá de vacaciones"
  return "Te toca trabajar"