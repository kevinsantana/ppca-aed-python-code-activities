"""
Usando uma função, faça um programa que leia 10 números inteiros e imprima na tela o maior deles. No caso de valores
iguais, imprima qualquer um dos maiores. Caso o maior número seja múltiplo do primeiro número n lido, imprima n na tela.

Entrada

Dez números inteiros, considere que o primeiro número lido nunca será 0.

Saída

O maior número 𝑚 e o primeiro número n lido, caso 𝑚=𝑎⋅𝑛,𝑎∈ℤ.
"""


def solve():
    numbers = []
    for _ in range(10):
        numbers.append(int(input()))
    m = max(numbers)
    print(m)
    if m % numbers[0] == 0:
        print(numbers[0])


if __name__ == "__main__":
    solve()
