def indice_do_maior(lista):
    if len(lista) == 1:
        return 0
    else:
        i = indice_do_maior(lista[:-1])
        if lista[-1] > lista[i]:
            i = len(lista) - 1
        return i

print(indice_do_maior(list(map(int, input().split()))))