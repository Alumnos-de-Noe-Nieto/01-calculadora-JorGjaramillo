def validar_repeticiones_vld(cadena: str) -> bool:
    return all(simbolo * 2 not in cadena for simbolo in "VLD")
