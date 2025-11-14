def soma_pares(lista):
    if len(lista) == 0:
        return 0
    
    ultimo = lista[-1]
    soma = 0
    if ultimo % 2 == 0:
        soma = soma + ultimo
    soma = soma + soma_pares(lista[:-1])
    return soma

list = list(map(int, input().split()))
print(soma_pares(list))