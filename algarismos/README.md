# Questão 4
Escreva uma função recursiva que determine quantos algarismos são necessários para representar um determinado
número, ignorando os zeros a esquerda. Exemplo: Para o número 12345 são necessários 5 algarismos.

Assinatura da função: def conta_algarismos(n)

Dica: A quantidade de algarismos de um número n é igual a 1+ o número n sem um algarismo (ou seja, ⌊n/10⌋
é n sem o último algarismo). Portanto, a função pode ser definida como:

conta_algarismos(n) =

1 Se n < 10

1 + conta_algarismos(⌊n/10⌋) Se n ≥ 10