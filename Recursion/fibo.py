
# 1st Method

# a =0
# b= 1
# n=5
# print(a, end=" ")
# def fibo(a,b,n):
#     if n==0:
#         return
    
#     print(b, end=" ")
    
#     fibo(b,a+b,n-1)

# fibo(a,b,n)


#2nd Method

def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)
        
    

print(fibo(8))

    