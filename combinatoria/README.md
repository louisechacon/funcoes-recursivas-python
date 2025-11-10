# Questão 6

Uma combinação sem repetição, em análise combinatória, é um subconjunto com $k$ elementos em um conjunto $U$, com $n$ elementos.[^1] A quantidade de subconjuntos distintos pode ser calculada pela fórmula:

$$
C_k^n = \frac{n!}{k! \times (n-k)!}
$$

Esta função pode ser definida recursivamente como:

$$
C_k^n =
\begin{cases}
  1 & \text{Se } n = k \\
  n & \text{Se } k = 1 \\
  C_{k-1}^{n-1} + C_k^{n-1} & \text{Se } 1 < k < n
\end{cases}
$$

* Escreva uma função recursiva que calcule o valor de $C_k^n$.
    * Assinatura da função: `def comb(n, k)`

[^1]: https://pt.wikipedia.org/wiki/Combinação