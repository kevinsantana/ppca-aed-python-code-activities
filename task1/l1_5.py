"""
Leia um valor inteiro N que lê a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois
inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X, inclusive o próprio X se ele for
ímpar. Por exemplo: para a entrada 4 5, a saída deve ser 45, que é equivalente a: 5 + 7 + 9 + 11 + 13, para a entrada
7 4, a saída deve ser 40, que é equivalente a: 7 + 9 + 11 + 13. No nal imprima também a maior e a menor soma, e a média
destas duas últimas somas.

Entrada:

A primeira linha de entrada é um inteiro N > 0 que é a quantidade de casos de teste que vem a seguir. Cada caso de teste
consiste em uma linha contendo dois inteiros X e Y, onde Y > 0.

Saída:

Imprima a soma S dos Y consecutivos números ímpares a partir do valor X, para cada X e Y lidos. Imprima também a maior e
a menor soma S. No final, imprima a média da maior e da menor soma com duas casas decimais após a vírgula, conforme
exemplo abaixo.
"""

from itertools import count


def solve():
    result = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        odd = []
        for i in count(x):
            if len(odd) == y:
                break
            if i % 2 != 0:
                odd.append(i)

        result.append(sum(odd))
        print(sum(odd))

    print(max(result), min(result), sep="\n")
    op = (max(result) + min(result)) / 2
    print(f"{op:.2f}")


if __name__ == "__main__":
    solve()
