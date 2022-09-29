"""
Faça um algoritmo que calcule o valor de expressões pós-fixas

Entrada:

Uma expressão pós fixa com números inteiros de 0 a 9 e as operações de adição e multiplicação, separados por espaços em
branco 

Saída:

número inteiro com o resultado da expressão
"""

import operator


def solve():
    operators = ["+", "*"]
    stack = []
    for exp in input().split():
        if exp not in operators:
            stack.append(int(exp))
        
        else:
            if exp == "+":
                res = operator.add(stack.pop(), stack.pop())
                stack.append(res)

            elif exp == "*":
                res = operator.mul(stack.pop(), stack.pop())
                stack.append(res)

    print(stack.pop())


if __name__ == "__main__":
    solve()
