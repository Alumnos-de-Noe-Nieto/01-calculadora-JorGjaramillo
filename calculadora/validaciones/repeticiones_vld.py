def validar_repeticiones_vld(cadena: str) -> bool:
    for simbolo in "VLD":
        if simbolo * 2 in cadena:
            return False
    return True