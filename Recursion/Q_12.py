# find the sum of first n natural nums



def sumOfN(n):
    if n <=1:
        return 1
    return n+ sumOfN(n-1)

print(sumOfN(10))


# definition: In a recurrence relation , if the problem is divided into linear sub-parts i.e. f(n)= a+ f(n-k) where a and k are constants, given k>1, then the recurrense relation is called linear rec relation

# def2:   If a rec relation has a problem divided into subparts which are fractions of the original problem size, then such a rec relation is called divide and concor rec relation