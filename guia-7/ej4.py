def peso_pino(altura_en_metros: float) -> float:
  altura_en_centimetros: float = altura_en_metros * 100

  if max(altura_en_centimetros, 3000) == 3000:
    return altura_en_centimetros * 3

  altura_sobre_3m_en_cm: float = altura_en_centimetros - 3000
  return altura_en_centimetros * 3 + altura_sobre_3m_en_cm * 2
  

def es_peso_util(peso_en_kg: float) -> bool:
  return peso_en_kg == max(peso_en_kg, 400) and peso_en_kg == min(peso_en_kg, 1000)

def sirve_pino(altura_en_metros: float) -> bool:
  return es_peso_util(peso_pino(altura_en_metros))

