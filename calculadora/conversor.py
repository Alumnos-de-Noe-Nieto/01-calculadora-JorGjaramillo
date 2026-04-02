from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos


def romano_a_entero(cadena: str) -> int:
    if not validar_simbolos(cadena):
        raise ExpresionInvalida("contiene símbolos inválidos")
    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida("repetición I/X/C/M inválida")
    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida("repetición V/L/D inválida")
    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida("orden descendente inválido")
    if not validar_restas(cadena):
        raise ExpresionInvalida("resta inválida")

    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    valor_previo = 0

    for simbolo in reversed(cadena):
        valor = valores[simbolo]
        if valor < valor_previo:
            resultado -= valor
        else:
            resultado += valor
        valor_previo = valor

    return resultado
