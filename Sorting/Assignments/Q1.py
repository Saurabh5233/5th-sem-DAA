# https://leetcode.com/problems/sort-colors/description/

# COLOR SORT

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(0,n):
            flag = False
            for j in range(0,n-i-1):
                if nums[j]> nums[j+1]:
                    flag = True
                    nums[j],nums[j+1] = nums[j+1], nums[j]
                    
            if(flag == False):
                break
        return nums
        