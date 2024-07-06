# find the product of the digits of a given number
n = 2169

def digitSum(n):
    if n==0:
        return 1
    return (n%10)* (digitSum(n//10))

print(digitSum(n))