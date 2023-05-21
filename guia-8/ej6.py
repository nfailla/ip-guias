def es_palindromo (palabra: str) -> bool:
  resultado: bool = True
  invertida: str = ""
  for i in range(len(palabra) - 1, -1, -1):
    invertida += palabra[i]
  for i in range(0, len(palabra)):
    if palabra[i] != invertida[i]:
      resultado = False
      
  return resultado
