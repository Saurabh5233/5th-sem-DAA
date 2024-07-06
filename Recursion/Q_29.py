# Perform Insertion Sort using Recursion


def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    
    # Sort the first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    last = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1
    
    arr[j + 1] = last

arr = [12, 11, 13, 5, 6]
insertion_sort_recursive(arr, len(arr))
print("Sorted array is:", arr)
