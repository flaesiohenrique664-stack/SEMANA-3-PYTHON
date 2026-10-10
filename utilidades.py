"""Funções utilitárias para conversões, validações e organização de dados."""


def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    """Converte uma temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9


def validar_senha(senha):
    """Valida se a senha tem ao menos 8 caracteres, uma letra e um número."""
    if not isinstance(senha, str):
        return False
    tem_letra = any(caractere.isalpha() for caractere in senha)
    tem_numero = any(caractere.isdigit() for caractere in senha)
    return len(senha) >= 8 and tem_letra and tem_numero


def total_caixa(*precos):
    """Soma uma quantidade variável de preços recebidos como argumentos."""
    return sum(precos)


def ficha_aluno(**dados):
    """Organiza os dados informados do aluno em um dicionário."""
    return dados


def adicionar_item_seguro(lista_original, item):
    """Retorna uma nova lista com o item, sem modificar a lista original."""
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista


def fatorial(numero):
    """Calcula o fatorial de um inteiro não negativo usando recursividade."""
    if not isinstance(numero, int) or isinstance(numero, bool) or numero < 0:
        raise ValueError("O número deve ser um inteiro não negativo.")
    if numero in (0, 1):
        return 1
    return numero * fatorial(numero - 1)


def relatorio(titulo, *linhas, **config):
    """Monta um relatório textual com linhas e opções de configuração.

    Opções reconhecidas em config:
        separador: texto usado entre as linhas (padrão: nova linha).
        maiusculo: se True, converte o título para maiúsculas.
    """
    separador = config.get("separador", "\n")
    titulo_final = titulo.upper() if config.get("maiusculo", False) else titulo
    conteudo = separador.join(str(linha) for linha in linhas)
    if conteudo:
        return f"{titulo_final}\\n{conteudo}"
    return titulo_final

if __name__ == "__main__":
    print("32 °C em Fahrenheit:", celsius_para_fahrenheit(32))
    print("Senha válida:", validar_senha("Python123"))
    print("Total da caixa:", total_caixa(2.50, 4.00, 3.25))
    print("Ficha:", ficha_aluno(nome="Ana", idade=19, curso="Engenharia"))
    original = ["lápis", "borracha"]
    copia = adicionar_item_seguro(original, "caderno")
    print("Lista original:", original)
    print("Nova lista:", copia)
    print("Fatorial de 5:", fatorial(5))
    print(relatorio("Resumo", "Item A", "Item B", separador=" | ", maiusculo=True))
