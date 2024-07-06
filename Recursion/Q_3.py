# Given two numbers x and y find the product using recursion

a = 12
b = 5

def product(a,b):
    if a==0 or b==0:
        return 0
    return  a+product(a,b-1)

print(product(a,b))