# Compute the factorial of a number using recursion

n=5

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n* factorial(n-1)

print(factorial(n))
