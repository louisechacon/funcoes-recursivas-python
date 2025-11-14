def palindromo(string):
    if len(string) == 1:
        return True
    if len(string) == 2:
        return string[0] == string[1]
    return (string[0] == string[-1]) and palindromo(string[1:-1])

print(palindromo(input()))