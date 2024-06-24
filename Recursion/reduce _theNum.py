

# n= 123

# def numberOfSteps(num,step) :
    
#     if num == 0:
#         return step
#     if num %2==0:
#         return numberOfSteps(num//2,step+1)
#     if num %2!= 0:
#         return numberOfSteps(num-1 ,step+1)

# print(numberOfSteps(n,0))

# using recursion , find the occurance of a digit in number n

n = 12521

def numOfOccur(n,tar,count):
    if n == 0:
        return count
    if n%10 == tar:
        return numOfOccur(n//10,tar,count+1)
    else:
        return numOfOccur(n//10,tar,count)

print(numOfOccur(n,2,0))
    