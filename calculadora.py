def _validar_numeros(a, b):
    for valor in (a, b):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("Los argumentos deben ser numéricos")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    _validar_numeros(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b