"""Funções estatísticas simples, sem dependências externas."""


def media(valores):
    """Retorna a média aritmética; retorna None para uma sequência vazia."""
    if not valores:
        return None
    return sum(valores) / len(valores)


def mediana(valores):
    """Retorna a mediana; retorna None para uma sequência vazia."""
    if not valores:
        return None
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    if len(ordenados) % 2 == 1:
        return ordenados[meio]
    return (ordenados[meio - 1] + ordenados[meio]) / 2


def moda(valores):
    """Retorna uma lista com todas as modas; lista vazia se não houver valores."""
    if not valores:
        return []
    frequencias = {valor: valores.count(valor) for valor in set(valores)}
    maior_frequencia = max(frequencias.values())
    if maior_frequencia == 1:
        return []
    return sorted(
        valor for valor, frequencia in frequencias.items()
        if frequencia == maior_frequencia
    )