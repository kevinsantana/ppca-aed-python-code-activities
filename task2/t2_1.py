"""
Usando a classe Pilha com os métodos empilha(item), desempilha(), tamanho() e estaVazio() implemente a funcao
decimal2binario(numero) que  converta números decimais em binário retornando o número binário como uma string de "0"s e
"1"s .
"""


def decimal2binario(numero):
    return "{0:b}".format(numero)
