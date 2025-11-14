def ordenada(lista):
    if len(lista) == 1:
        return True
    
    ultimo = lista[-1]
    penultimo = lista[-2]
    if ultimo > penultimo:
        return True and ordenada(lista[:-1])
    else:
        return False
    
list = list(map(int, input().split()))
print(ordenada(list))