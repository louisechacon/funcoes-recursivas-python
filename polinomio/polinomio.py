def polinomio(coeficientes, x):
    if len(coeficientes) == 1:
        return coeficientes[0]
    return x * polinomio(coeficientes[:-1], x) + coeficientes[-1]

coef = list(map(int, input().split()))
k = int(input())
print(polinomio(coef,k))