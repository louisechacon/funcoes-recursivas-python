def conta_divisores_r(n, divisor):
    if divisor == 1:
        return [1]
    else:
        if n % divisor == 0:
            return conta_divisores_r(n, divisor-1) + [divisor]
        else:
            return conta_divisores_r(n, divisor-1)

def conta_divisores(n):
    return conta_divisores_r(n,n)
print(conta_divisores(int(input())))