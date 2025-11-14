def ocorrencias(lista, x):
    if len(lista) == 0:
        return 0
    
    ultimo = lista[-1]
    if ultimo == x:
        return 1 + ocorrencias(lista[:-1], x)
    else:
        return ocorrencias(lista[:-1], x)
    
l = list(map(int, input().split()))
k = int(input())
print(ocorrencias(l, k))