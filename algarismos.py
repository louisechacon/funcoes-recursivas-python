def conta_algarismos_r(n):
    if n < 10:
        return 1
    else:
        return 1 + conta_algarismos_r(n/10)

def conta_algarismos(n):
    return conta_algarismos_r(n)
print(conta_algarismos(int(input())))