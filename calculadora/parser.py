from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    """
    Representa un token en una expresión aritmética de números romanos.

    Attributes:
        tipo: El tipo de token ("ROMANO", "SUMA", "RESTA", "ESPACIO")
        valor: El valor del token (cadena)
        posicion: La posición del token en la expresión original
    """

    tipo: str
    valor: str
    posicion: int


def evaluar_expresion(expresion: str) -> list[Token]:
    tokens = tokenizar_expresion(expresion)
    filtrados = [t for t in tokens if t.tipo != 'ESPACIO']
    if not filtrados:
        return []
    if not validar_estructura_tokens(tokens):
        raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')
    return tokens


def tokenizar_expresion(expresion: str) -> list[Token]:
    tokens = []
    i = 0
    while i < len(expresion):
        if expresion[i] == ' ':
            tokens.append(Token('ESPACIO', ' ', i))
            i += 1
        elif expresion[i] == '+':
            tokens.append(Token('SUMA', '+', i))
            i += 1
        elif expresion[i] == '-':
            tokens.append(Token('RESTA', '-', i))
            i += 1
        elif expresion[i] in 'IVXLCDM':
            inicio = i
            while i < len(expresion) and expresion[i] in 'IVXLCDM':
                i += 1
            tokens.append(Token('ROMANO', expresion[inicio:i], inicio))
        else:
            raise ExpresionInvalida(f"Carácter inválido '{expresion[i]}' en posición {i}")
    return tokens


def validar_estructura_tokens(tokens: list[Token]) -> bool:
    filtrados = [t for t in tokens if t.tipo != 'ESPACIO']
    if len(filtrados) < 3:
        return False
    if len(filtrados) % 2 == 0:
        return False
    if filtrados[0].tipo != 'ROMANO':
        return False
    if filtrados[-1].tipo != 'ROMANO':
        return False
    for i, token in enumerate(filtrados):
        if i % 2 == 0 and token.tipo != 'ROMANO':
            return False
        if i % 2 != 0 and token.tipo not in ('SUMA', 'RESTA'):
            return False
    return True
