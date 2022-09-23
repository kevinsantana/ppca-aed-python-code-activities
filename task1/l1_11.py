"""
Entrada:

A entrada contém uma linha com 2 inteiros n (1 <= n <= 1000) e m (1 <= m <= 1000) indicando, respectivamente, a
quantidade de figurinhas que Raphael e Luiza têm para trocar.

Saída:

A saída será o tamanho máximo da pilha de figurinhas que poderia ser trocada entre dois jogadores.
"""
from math import gcd


def solve():
    n, m = map(int, input().split())
    print(gcd(n, m))


if __name__ == '__main__':
    solve()
