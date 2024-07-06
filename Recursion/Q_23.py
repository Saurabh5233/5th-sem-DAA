# Find mean of Array elements using recursion

arr =[1,2,3,4,5]
n  = len(arr)
sum = 0

def sumofArray(arr,sum):
    if arr ==[]:
        return sum  
    sum+= arr.pop()
    return sumofArray(arr,sum)


mean = sumofArray(arr,sum)/n
print(mean)
