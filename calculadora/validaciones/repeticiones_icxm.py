def validar_repeticiones_icxm(cadena: str) -> bool:
    return all(simbolo * 4 not in cadena for simbolo in "IXCM")
