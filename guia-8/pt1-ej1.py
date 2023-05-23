# 1)
def pertenece(s: list[int], e: int) -> bool:
    i: int = 0
    encontrado: bool = False
    while i < len(s) or encontrado:
        i += 1
        if s[i] == e:
            encontrado = True


# 2)
def divideATodos(s: list[int], e: int) -> bool:
    # for el in s: # se puede usar???
    resultado: bool = True
    for i in range(0, len(s)):
        if s[i] % e != 0:
            resultado = False

    return resultado


# 3)
def sumaTotal(s: list[int]) -> bool:
    suma: int = 0
    for i in range(0, len(s)):
        suma += s[i]

    return suma


# 4)
def ordenados(s: list[int]) -> bool:
    resultado: bool = True
    for i in range(0, len(s) - 1):
        if not s[i] < s[i + 1]:
            resultado = False

    return resultado


# 5)
def alguna_mayor_a_7(palabras: list[str]) -> bool:
    resultado: bool = False
    i: int = 0
    while not resultado and i < len(palabras):
        i += 1
        if len(palabras[i]) > 7:
            resultado = True
    return resultado


# 6)
def es_palindromo(palabra: str) -> bool:
    resultado: bool = True
    invertida: str = ""
    for i in range(len(palabra) - 1, -1, -1):
        invertida += palabra[i]
    for i in range(0, len(palabra)):
        if palabra[i] != invertida[i]:
            resultado = False

    return resultado


# 7)
def fortaleza_contrasenia(contrasenia: str) -> str:
    # qué onda con la ñ/Ñ? hay que validarla aparte?
    if len(contrasenia) < 5:
        return "ROJA"

    if (
        len(contrasenia) > 8
        and tiene_alguna_minuscula(contrasenia)
        and tiene_alguna_mayuscula(contrasenia)
        and tiene_algun_numero(contrasenia)
    ):
        return "VERDE"

    return "AMARILLA"


def tiene_alguna_minuscula(palabra: str) -> bool:
    resultado: bool = False
    for i in range(0, len(palabra)):
        if palabra[i] >= "a" and palabra[i] <= "z":
            resultado = True

    return resultado


def tiene_alguna_mayuscula(palabra: str) -> bool:
    resultado: bool = False
    for i in range(0, len(palabra)):
        if palabra[i] >= "A" and palabra[i] <= "Z":
            resultado = True

    return resultado


def tiene_algun_numero(palabra: str) -> bool:
    resultado: bool = False
    for i in range(0, len(palabra)):
        if palabra[i] >= "0" and palabra[i] <= "9":  # el rango es 0..9 ó 1..0???
            resultado = True

    return resultado


# 8)
def calcular_saldo_actual(movimientos: list[tuple[str, float]]) -> float:
    saldo_actual: float = 0

    for i in range(0, len(movimientos)):
        operacion: str = movimientos[i][0]
        monto: float = movimientos[i][1]
        if operacion == "I":
            saldo_actual += monto
        else:
            saldo_actual -= monto

    return saldo_actual


# 9)
def tiene_al_menos_tres_vocales_distintas(palabra: str) -> bool:
    vocales: list[str] = ["a", "e", "i", "o", "u"]
    cantidad_apariciones_diferentes: int = 0
    for i in range(0, vocales):
        cantidad_apariciones_vocal: int = palabra.lower().count(vocales[i])
        cantidad_apariciones_diferentes += min(1, cantidad_apariciones_vocal)

    return cantidad_apariciones_diferentes
