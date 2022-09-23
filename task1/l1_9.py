"""
Dado duas strings s1 e s2, o trecho de codigo acima escreve na tela parte do que é especificado em Saída.

Entrada

A entrada consistirá apenas de duas strings  s1 e s2. Não terá como entrada duas strings iguais.

Saída

Escreva na tela  s1 concatenada com s2, o reverso de  s1 e se  s1 é prefixo de s2. No primeiro exemplo  s1 é a string
vazia (nil).
"""


def solve():
    s1 = input()
    s2 = input()
    print(f"{s1}{s2}")
    if s1:
        print(''.join(reversed(list(s1))))
    else:
        print(' ')
    if s1 in s2[:-1]:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    solve()
