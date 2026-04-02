def validar_orden_descendente(cadena: str) -> bool:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones_validas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    i = 0
    while i < len(cadena) - 1:
        par = cadena[i:i+2]
        if par in sustracciones_validas:
            if i > 0 and cadena[i-1] == cadena[i]:
                return False
            valor_sustraccion = valores[cadena[i+1]] - valores[cadena[i]]
            if i + 2 < len(cadena) and valores[cadena[i+2]] > valores[cadena[i+1]] - valor_sustraccion:
                return False
            i += 2
        else:
            if valores[cadena[i]] < valores[cadena[i+1]]:
                return False
            i += 1
    return True
