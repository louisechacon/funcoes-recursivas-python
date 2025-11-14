def primo_r(n, divisor):
    if n == 1:
        return False
    if divisor == 1:
        return True
    else:
        if n % divisor == 0:
            if divisor == n:
                return True and primo_r(n, divisor-1)
            else:
                return False
        else:
            return True and primo_r(n,divisor-1)

def primo(n):
    return primo_r(n,n)


def primos(lista):
    if len(lista) == 0:
        return []
    ultimo = lista[-1]
    l2 = []
    if primo(ultimo):
        l2 = l2 + [ultimo]
    return primos(lista[:-1]) + l2

list = list(map(int, input().split()))
print(primos(list))