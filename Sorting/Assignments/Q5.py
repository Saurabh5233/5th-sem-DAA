# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

# sort-even-and-odd-indices-independently



class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        oddArr =[]
        evenArr = []
        for i in range(n):
            if i%2==0:
                evenArr.append(nums[i])
            else:
                oddArr.append(nums[i])
        
        oddArr.sort(reverse = True)
        evenArr.sort()
        
        for i in range(len(nums)):
            if i%2==0:
                nums[i] = evenArr.pop(0)
            else:
                nums[i] = oddArr.pop(0)
            
        
        return nums