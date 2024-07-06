from typing import List


def Sort(arr:List[int])->List[int]:
    l = 0
    h = len(arr)-1
    
    
    return divide(arr,l,h)

def divide(arr:List[int],l:int,h:int)->List[int]:
    if l<h:
        m= l+ (h-l)//2
        
        divide(arr,l,m)
        divide(arr,m+1,h)
        merge(arr,l,m,h)
    return arr

def merge(arr:List[int],l:int,m:int,h:int)->List[int]:
    left = arr[l:m + 1]
    right = arr[m + 1:h + 1]
    
    i = j = 0
    k = l
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# the below merge function will work when arrays are passed as halves not the pointers.......

# def merge(left,right):
#     result = []
#     i=j=0
#     while i<len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#         result.extend(left[i:])
#         result.extend(left[j:])
        

    
    
    
    
        
arr = [4,5,3,2,6,7]
print(Sort(arr))
        