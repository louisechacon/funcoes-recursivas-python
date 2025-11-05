def conta_bits_r(n):
    if n <= 1:
        return 1
    else:
        return 1 + conta_bits_r(n // 2)

def conta_bits(n):
    return conta_bits_r(n)
print(conta_bits(int(input())))