"""
Entrada:

Inteiro n > 0, onde n representa os meses que passaram.

Saída:

Será impresso na tela o número de casais após n meses e o valor de n! na mesma linha.

Caso o número de casais de coelhos seja par, será impresso também, na mesma linha, quantos novos casais irão nascer no
próximo mês.
"""
from math import factorial
from functools import lru_cache


@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def solve():
    n = int(input())
    fibo_n = fibonacci(n)
    if fibo_n % 2 == 0:
        fibo_n1 = fibonacci(n+1)
        next_month = fibo_n1 - fibo_n
        print(fibo_n, factorial(n), next_month)
    else:
        print(fibo_n, factorial(n))


if __name__ == '__main__':
    solve()
