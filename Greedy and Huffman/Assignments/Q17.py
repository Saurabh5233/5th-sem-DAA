# https://leetcode.com/problems/jump-game/description/

# Jump Game

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return farthest >= len(nums) - 1

# Example usage:
sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))  # Output: true
print(sol.canJump([3, 2, 1, 0, 4]))  # Output: false
