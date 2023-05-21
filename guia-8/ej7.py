def fortaleza_contrasenia (contrasenia: str) -> str:
  # qué onda con la ñ/Ñ? hay que validarla aparte?
  if len(contrasenia) < 5:
    return "ROJA"
  
  if len(contrasenia) > 8 and tiene_alguna_minuscula(contrasenia) and tiene_alguna_mayuscula(contrasenia) and  tiene_algun_numero(contrasenia):
    return "VERDE"
  
  return "AMARILLA"

def tiene_alguna_minuscula (palabra: str) -> bool:
  resultado: bool = False
  for i in range(0, len(palabra)):
    if palabra[i] >= "a" and palabra[i] <= "z":
      resultado = True
      
  return resultado

def tiene_alguna_mayuscula (palabra: str) -> bool:
  resultado: bool = False
  for i in range(0, len(palabra)):
    if palabra[i] >= "A" and palabra[i] <= "Z":
      resultado = True

  return resultado

def tiene_algun_numero (palabra: str) -> bool:
  resultado: bool = False
  for i in range(0, len(palabra)):
    if palabra[i] >= "0" and palabra[i] <= "9": # el rango es 0..9 ó 1..0???
      resultado = True

  return resultado
