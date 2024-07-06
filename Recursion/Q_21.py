# Number of Steps to Reduce a Number to Zero using recursion

n= 123

def numberOfSteps(num,step) :
    
    if num == 0:
        return step
    if num %2==0:
        return numberOfSteps(num//2,step+1)
    if num %2!= 0:
        return numberOfSteps(num-1 ,step+1)

print(numberOfSteps(n,0))

