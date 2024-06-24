# Given a sorted array and an int target , write a recutsive function to find the target and return the index, if not found return -1

arr = [-1,2,5,0,9,12,15]
tar = 0
s = 0
e= (len(arr)-1)
def binSearch(arr,s,e):
    if s>e:
        return -1
    mid = s + (e-s)//2
    if arr[mid] == tar:
        return mid
    elif tar < arr[mid]:
        return binSearch(arr,s,mid-1)
    elif tar > arr[mid]:
        return binSearch(arr,mid+1,e)


print(binSearch(arr,s,e))