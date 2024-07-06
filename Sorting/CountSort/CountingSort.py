from typing import List

def counting_sort(nums: List[int]) -> List[int]:
    N = len(nums)
    if N == 0:
        return nums
    K = max(nums)+1
    # Initialing a frequency counting array
    count = [0]*K
    for x in nums:
        count[x] += 1
    
    # Result Array for storing the sorted array
    res = [0]*N
    i=0
    for x in range(K):
        for c in range(count[x]):
            res[i]= x
            i +=1
    return res

nums = [2,0,3,0,1,1,5,3,11]
print(counting_sort(nums))

    