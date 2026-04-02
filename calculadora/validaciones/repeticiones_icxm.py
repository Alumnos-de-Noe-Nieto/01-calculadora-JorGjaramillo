def validar_repeticiones_icxm(cadena: str) -> bool:
    for simbolo in "IXCM":
        if simbolo * 4 in cadena:
            return False
    return True