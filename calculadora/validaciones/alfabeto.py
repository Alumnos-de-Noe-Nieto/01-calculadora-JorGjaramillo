def validar_simbolos(cadena: str) -> bool:
    cadena = cadena.strip()
    if not cadena:
        return False
    return set(cadena).issubset("IVXLCDM")
