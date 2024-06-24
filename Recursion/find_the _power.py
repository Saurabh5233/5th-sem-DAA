a=14
b=2

def pow(a,b):
    if b==0:
        return 1
    return a*pow(a,b-1)

print(pow(a,b))