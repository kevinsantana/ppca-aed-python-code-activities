"""
Leia quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano:
(x 1 , y 1 ) e (x 2 , y 2 ) e calcule a distância entre eles, mostrando 4 casas decimais após a
virgula, segundo a fórmula:

Distancia = ((x2 - x1 )2 + (y2 - y1 )2)1/2
Python possui complex como tipo de dados. Um número complexo tem um componente
real e imaginário, ambos representados pelo tipo float em Python (é possivel acessá-los
separadamente). Leia também um número complexo z = a + bj e calcule seu módulo |z|
(distância até a origem), mostrando 4 casas decimais após a virgula, usando a fórmula:

|z| = ((a 2 + b 2 ))1/2

Entrada:

A entrada contém três linhas de dados. A primeira linha contém dois valores de ponto
flutuante x1 e y1 , a segunda também contém dois valores de ponto flutuante x2 e y2 e a
terceira contém um número complexo.

Saida:

Calcule e imprima o valor da distância e do módulo segundo as fórmulas fornecidas, com
4 casas decimais.

Nota:
Para ler vários valores em uma mesma linha, use input().split(). Se o argumento de
split for vazio, o separador das variáveis é um espaço em branco. Porém, lembre-se que
input lê apenas strings do teclado, portanto você deverá converter as strings em floats.
No exemplo a seguir, o usuário digita valores separados por um espaço em branco e aperta
enter para enviá-los, então, o programa lê esses valores separados por espaços como strings
(na ordem em que aparecem), guardados nas variáveis correspondentes e os converte para
floats:
A, B, C = input().split()
A, B, C = [float(A), float(B), float(C)]
"""

from math import sqrt


def solve(x1, y1, x2, y2, z):
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    z = sqrt(z.real**2 + z.imag**2)
    return f"{d:.4f}", f"{z:.4f}"


if __name__ == "__main__":
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    z = complex(input())
    r1, r2 = solve(x1, y1, x2, y2, z)
    print(r1, r2, sep="\n")
