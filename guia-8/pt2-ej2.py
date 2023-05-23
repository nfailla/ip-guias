# 1)
def cerificar_posiciones_pares_inout(nros: list[float]) -> None:
    for i in range(0, len(nros)):
        if i % 2 == 0:
            nros[i] = 0


# 2)
def cerificar_posiciones_pares_in(nros: list[float]) -> list[float]:
    res: list[float] = []
    for i in range(0, len(nros)):
        if i % 2 == 0:
            res.append(0)
        else:
            res.append(nros[i])

    return res


# 3)
def quitar_vocales(texto: str) -> str:
    res: str = ""
    for i in range(0, len(texto)):
        if ["a", "e", "i", "o", "u"].count(texto[i].lower()) == 0:
            res += texto[i]

    return res


# 4)
def reemplaza_vocales(texto: str) -> str:
    res: str = ""
    for i in range(0, len(texto)):
        if ["a", "e", "i", "o", "u"].count(texto[i].lower()) == 0:
            res += texto[i]
        else:
            res += "_"

    return res


# 5)
def da_vuelta_str(texto: str) -> str:
    res: str = ""
    for i in range(len(texto) - 1, -1, -1):
        res += texto[i]

    return res
