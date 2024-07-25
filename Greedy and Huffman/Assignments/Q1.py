# You are given an array of integers and an integer k. Your task is to select k elements from the array such that their sum is maximized


from typing import List

def maxSum(nums: List[int],k: int)->int:
    nums.sort()
    sum = 0
    for i in range(k):
        sum+= nums[i]
    
    return sum

nums = [2,3,4,5,1,6]
print(maxSum(nums,3))