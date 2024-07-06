# from typing import List
arr = [6,45,4,6,4,6,3]

def bubble(arr):
    n = len(arr)
    for i in range(0,n):
        flag = False
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                flag = True
                arr[j],arr[j+1] = arr[j+1], arr[j]
                
        if(flag == False):
            break

bubble(arr)
print(arr)

# bubble sort is also called as sinking or exchange sort