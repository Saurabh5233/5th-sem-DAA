# Find sum of Array elements using recursion

arr =[1,2,3,4,5]
sum = 0

def sumofArray(arr,sum):
    if arr ==[]:
        return sum  
    sum+= arr.pop()
    return sumofArray(arr,sum)

print(sumofArray(arr,sum))
