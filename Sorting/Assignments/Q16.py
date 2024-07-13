# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

# Find All Numbers Disappeared in an Array


from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        missing_numbers = [i + 1 for i in range(n) if nums[i] > 0]
        
        return missing_numbers


