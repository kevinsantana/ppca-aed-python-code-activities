"""
Faça um programa que peça ao usuário para informar dois números reais, conforme especiﬁcado em Entrada. Depois calcule a
média desses números e mostre-a na tela, conforme especiﬁcado em Saída.

Entrada:

Leia 2 números reais do teclado, um por linha.

Saída:

Imprima na tela media, onde media é um real com duas casas decimais que representa a média dos dois reais lidos do teclado
"""


def solve(a: int, b: int):
    op = (a + b) / 2
    return f"{op:.2f}"


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    print(solve(a, b))
