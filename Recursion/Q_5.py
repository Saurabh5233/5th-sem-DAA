# convert into binary

n = 235

def bin(n):
    if n==0:
        return 0
    return n%2+ 10*(bin(n//2))

print(bin(n))