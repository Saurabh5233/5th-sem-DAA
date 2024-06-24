# reverse a given number using recursion

import math

n = 257954544789
k = math.floor(math.log10(n)) + 1

def reverse(n, k):
    if n < 10:
        return n
    d = n % 10
    return d * 10**(k-1) + reverse(n // 10, k-1)

print(reverse(n, k))
