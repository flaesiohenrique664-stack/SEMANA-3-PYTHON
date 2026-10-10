"""Script principal: demonstra importação e reaproveitamento dos módulos."""

import calculadora
import estatistica as est
import utilidades


def main():
    """Executa exemplos de todas as funções do projeto."""
    print("=== CALCULADORA ===")
    print("10 + 5 =", calculadora.somar(10, 5))
    print("10 - 5 =", calculadora.subtrair(10, 5))
    print("10 * 5 =", calculadora.multiplicar(10, 5))
    resultado_divisao = calculadora.dividir(10, 0)
    if resultado_divisao is None:
        print("Divisão: não é possível dividir por zero.")
    else:
        print("10 / 0 =", resultado_divisao)

    print("\\n=== UTILIDADES ===")
    print("25 °C em Fahrenheit:", utilidades.celsius_para_fahrenheit(25))
    print("77 °F em Celsius:", utilidades.fahrenheit_para_celsius(77))
    print("Senha válida:", utilidades.validar_senha("Python123"))
    print("Total da caixa:", utilidades.total_caixa(12.50, 7.25, 3.00))
    print(
        "Ficha do aluno:",
        utilidades.ficha_aluno(nome="Ana", idade=19, curso="Engenharia da Computação"),
    )

    lista_original = ["caderno", "caneta"]
    lista_nova = utilidades.adicionar_item_seguro(lista_original, "régua")
    print("Lista original:", lista_original)
    print("Lista nova:", lista_nova)

    print("Fatorial de 5:", utilidades.fatorial(5))
    print(
        utilidades.relatorio(
            "Relatório de exemplo",
            "Primeira linha",
            "Segunda linha",
            separador="\n- ",
            maiusculo=True,
        )
    )

    print("\\n=== ESTATÍSTICA (alias est) ===")
    numeros = [4, 2, 7, 2, 9, 2]
    print("Valores:", numeros)
    print("Média:", est.media(numeros))
    print("Mediana:", est.mediana(numeros))
    print("Moda:", est.moda(numeros))


if __name__ == "__main__":
    main()
