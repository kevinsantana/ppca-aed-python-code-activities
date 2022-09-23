"""
Faça um programa que leia 5 números reais e calcule a média ponderada desses números,
usando apenas duas variáveis.

Entrada:

A entrada contém cinco números reais: x1 , x2 , x3 , x4 e x5.

Saida

Calcule e imprima a média m (com 3 casas decimais) usando a fórmula:

m=(1x1 + 2x2 + 3x3 + 4x4 + 5x5)/15
"""


def solve(numbers):
    a, b, c, d, e = numbers
    m = (1 * a + 2 * b + 3 * c + 4 * d + 5 * e) / 15
    return f"{m:.3f}"


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    print(solve((a,b,c,d,e)))
