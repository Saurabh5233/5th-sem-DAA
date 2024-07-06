# Find the value of 'a' raised to the power 'b' using recursion

a=14
b=-3

def pow(a,b):
    if b==0:
        return 1
    if b== 1:
        return a
    if (b<0):
        a =1/a
        b=-b
    return powerhelp(a,b)

def powerhelp(a,b):
    if b== 0:
        return 1
    half = powerhelp(a,b//2)
    #for even divisor
    if b%2==0:
        return half*half
    # for odd divisor
    else:
        return half*half*a

print(pow(a,b))