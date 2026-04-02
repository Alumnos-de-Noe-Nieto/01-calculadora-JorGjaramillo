def validar_orden_descendente(cadena: str) -> bool:
    VALORES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    SUSTRACCIONES_VALIDAS = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    i = 0
    while i < len(cadena) - 1:
        par = cadena[i:i+2]
        if par in SUSTRACCIONES_VALIDAS:
            if i > 0 and cadena[i-1] == cadena[i]:
                return False
            valor_sustraccion = VALORES[cadena[i+1]] - VALORES[cadena[i]]
            if i + 2 < len(cadena) and VALORES[cadena[i+2]] > VALORES[cadena[i+1]] - valor_sustraccion:
                return False
            i += 2
        else:
            if VALORES[cadena[i]] < VALORES[cadena[i+1]]:
                return False
            i += 1
    return True