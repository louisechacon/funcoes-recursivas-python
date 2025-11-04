def primo_r(n, divisor):
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
print(primo(5))