"""
Um pequeno jogo de adivinhação funciona da seguinte forma: você deﬁne um número n e chama um amigo, que deverá adivinhar
o número escolhido. Faça um programa que peça um inteiro e então ﬁque pedindo que um usuário tente adivinhá-lo até que
acerte. Em cada tentativa o programa deve dizer se o chute foi maior ou menor que o número certo.

Entrada:

A primeira linha de entrada será o inteiro n, que deverá ser adivinhado. As próximas linhas serão os números chutados
pelo jogador, que continuará chutando números até que adivinhe o número correto.

Saída:

Se o número digitado for menor que n apresente a mensagem: “O número correto é maior.”. Se o nuúmero digitado for maior
que n apresente a mensagem: “O número correto é menor.”. Quando o usuário acertar o número imprima: “Parabéns! Você acertou.”.
"""


def solve():
    n = int(input())

    while True:
        kick = int(input())

        if kick < n:
            print("O número correto é maior.")
        elif kick > n:
            print("O número correto é menor.")
        elif n == kick:
            print("Parabéns! Você acertou.")
            break


if __name__ == "__main__":
    solve()
