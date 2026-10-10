"""Operações matemáticas básicas para reutilização em outros scripts."""


def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a diferença entre dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b


def dividir(a, b):
    """Divide a por b; retorna None se o divisor for zero."""
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    print("Teste da calculadora:")
    print("Soma:", somar(10, 5))
    print("Subtração:", subtrair(10, 5))
    print("Multiplicação:", multiplicar(10, 5))
    resultado = dividir(10, 0)
    print("Divisão por zero:", "divisor não pode ser zero" if resultado is None else resultado)
