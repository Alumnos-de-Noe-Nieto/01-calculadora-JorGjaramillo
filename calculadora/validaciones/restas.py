def validar_restas(cadena: str) -> bool:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones_validas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    i = 0
    while i < len(cadena):
        if i + 1 < len(cadena) and valores[cadena[i]] < valores[cadena[i+1]]:
            if cadena[i:i+2] not in sustracciones_validas:
                return False
            if i > 0 and cadena[i-1] == cadena[i]:
                return False
            i += 2
        else:
            i += 1
    return True
