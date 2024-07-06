# Reverse Count down of a given number using recursion
n = 12

def countDown(n):
    if n<= 0:
        print(0)
        return
    countDown(n-1)
    print(n)

countDown(n)
    