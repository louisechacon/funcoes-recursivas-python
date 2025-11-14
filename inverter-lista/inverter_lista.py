def inverter_lista(lista):
    if len(lista) == 0:
        return []
    return lista[-1:] + inverter_lista(lista[:-1])
    
l = list(map(int, input().split()))
print(inverter_lista(l))