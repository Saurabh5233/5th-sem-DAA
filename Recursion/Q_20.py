# using recursion , find the occurance of a digit in number n

n = 1000001
tar =0

def numOfOccur(n,tar,count):
    if n == 0:
        return count
    if n%10 == tar:
        return numOfOccur(n//10,tar,count+1)
    else:
        return numOfOccur(n//10,tar,count)

print(numOfOccur(n,tar,0))
    