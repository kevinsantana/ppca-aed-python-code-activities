"""
Escreva uma função compare que dado dois números x e y, retorne 1 se x for maior que y, 0 se for igual a y, e -1 se x
for menor que y

Usando o retorno da função, imprima na tela: "x e maior que y" se o retorno for 1, "x e igual a y" se o retorno for 0, e
"x e menor que y", caso contrário.

Entrada

Duas linhas de entrada correspondentes aos inteiros x
e y

.

Saída

Será impresso na tela a mensagem "x e maior que y" se o retorno da função for 1, "x e igual a y" se o retorno da função
for 0, e "x e menor que y", caso contrário.
"""


def solve():
    x = int(input())
    y = int(input())
    result = {
        x > y: "x e maior que y",
        x == y: "x e igual a y",
        x < y: "x e menor que y",
    }
    return result.get(True)


if __name__ == "__main__":
    print(solve())
