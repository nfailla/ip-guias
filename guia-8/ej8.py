def calcular_saldo_actual (movimientos: list[tuple[str, float]]) -> float:
  saldo_actual: float = 0

  for i in range(0, len(movimientos)):
    operacion: str = movimientos[i][0]
    monto: float = movimientos[i][1]
    if operacion == "I":
      saldo_actual += monto
    else:
      saldo_actual -= monto
      
  return saldo_actual
