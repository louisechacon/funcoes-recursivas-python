# Questão 15
Seja o polinômio

Pn(x) = a0x
n + a1x
n−1 + a2x
n−2 + . . . + an−1x + an

Que pode ser calculado através da definição recursiva a seguir:
Pn(x) = x.Pn−1(x) + an

onde

Pn−1(x) = a0x
n−1 + a1x
n−2 + . . . + an−2x + an−1

Escreva uma função recursiva Pn(x). A função deve receber como parâmetro uma lista (array) com os coeficientes
do polinômio e o valor de x.

Assinatura da função: def polinomio(coeficientes,x)