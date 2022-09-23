"""
No caminho para encontrar Jon Snow em Dragonstone, o lobo Ghost enfrenta um problema: uma grande escada. Os degraus da
escada são numeradas de 1 até infnito. Sendo um lobo esperto, Ghost decidiu calcular dois valores, o número de degraus
percorridos com números pares e ímpares.

Você precisa checar se o número de passos em degraus pares e ímpares encontrados pelo Ghost estão corretos. Considere que
ele não pula nenhum degrau e que ele sobe pelo menos o degrau de núumero 1.

Entrada

Em uma única linha são dados dois inteiros a, b (0  ≤ a,b ≤ 100), o número de passos pares e ímpares, respectivamente.

Saída

Em uma única linha, imprima "a b ok", se Ghost calculou corretamente os valores e "a b errados" caso contrário.
"""
from math import floor


def solve():
    odd, even = 0, 0
    a, b = map(int, input().split())
    steps = a + b

    if steps % 2 == 0:
        odd = even = floor(steps / 2)
    else:
        odd, even = floor(steps / 2) + 1, floor(steps / 2)

    if a == 0 and b == 0:
        print(a, b, "errados")
        return

    if even == a and odd == b:
        print(a, b, "ok")
    else:
        print(a, b, "errados")


if __name__ == "__main__":
    solve()
