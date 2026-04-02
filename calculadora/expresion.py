
from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    tokens = parsear_expresion(expresion)
    filtrados = [t for t in tokens if t.tipo != 'ESPACIO']

    if not filtrados:
        raise ExpresionInvalida("la expresión está vacía")

    resultado = romano_a_entero(filtrados[0].valor)

    i = 1
    while i < len(filtrados):
        operador = filtrados[i]
        numero = romano_a_entero(filtrados[i + 1].valor)
        if operador.tipo == 'SUMA':
            resultado += numero
        elif operador.tipo == 'RESTA':
            resultado -= numero
        i += 2

    if resultado <= 0:
        raise ExpresionInvalida("el resultado de la expresión es negativo o cero")

    return resultado
