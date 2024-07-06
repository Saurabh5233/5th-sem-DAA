# https://www.geeksforgeeks.org/sum-triangle-from-array/

# Sum triangle from array

from typing import List

def TriangleArr(arr:List[int])->List[int]:
    n = len(arr)
    
    if n <=1:
        return arr
    
    temp = []
    for i in range(0,n-1):
        temp.append(arr[i] + arr[i+1])
    
    TriangleArr(temp)
    
    print(temp)
    
    
arr = [2,3,4,5,6,7]
TriangleArr(arr)