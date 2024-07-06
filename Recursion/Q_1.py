# find the sum of the digits of a given number
n = 2069

def digitSum(n):
    if n==0:
        return 0
    return n%10+ digitSum(n//10)

print(digitSum(n))