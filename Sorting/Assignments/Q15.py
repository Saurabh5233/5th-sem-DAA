# https://leetcode.com/problems/set-mismatch/description/


# Set Mismatch

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        expected_sum_squares = n * (n + 1) * (2 * n + 1) // 6
        
        actual_sum = sum(nums)
        actual_sum_squares = sum(x * x for x in nums)
        
        diff1 = expected_sum - actual_sum
        diff2 = expected_sum_squares - actual_sum_squares
        
        sum_xy = diff2 // diff1
        
        x = (sum_xy - diff1) // 2
        y = sum_xy - x
        
        return [x, y]

