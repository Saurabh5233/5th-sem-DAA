# https://leetcode.com/problems/minimum-number-game/

# MINIMUM NUMBER GAME

# class Solution(object):
#     def numberGame(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         arr =[]
#         # nums.sort()
        
        
#         a,b = 0,1
#         while a<len(nums) and b < len(nums):
#             arr.append(nums[b])
#             arr.append(nums[a])
#             a+=2
#             b+=2
#         return arr

        
class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr =[]
        # nums.sort()
        self.bubble(nums)  #USING BUBBLE SORT...........
        a,b = 0,1
        while a<len(nums) and b < len(nums):
            arr.append(nums[b])
            arr.append(nums[a])
            a+=2
            b+=2
        return arr

    def bubble(self, arr):
        n = len(arr)
        for i in range(0,n):
            flag = False
            for j in range(0,n-i-1):
                if arr[j]> arr[j+1]:
                    flag = True
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                    
            if(flag == False):
                break
        