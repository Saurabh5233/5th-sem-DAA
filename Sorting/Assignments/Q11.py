# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/


# Special Array With X Elements Greater Than or Equal X

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for x in range(1, n + 1):
            # Find the number of elements greater than or equal to x
            count = sum(1 for num in nums if num >= x)
            if count == x:
                return x
        
        return -1
