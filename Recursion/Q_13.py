# https://leetcode.com/problems/powx-n/

# Find the value of 'a' raised to the power 'b' using recursion

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n== 1:
            return x
        if (n<0):
            x =1/x
            n=-n
        return self.powerhelp(x,n)

    def powerhelp(self,x,n):
        if n== 0:
            return 1
        half = self.powerhelp(x,n//2)
        #for even divisor
        if n%2==0:
            return half*half
        # for odd divisor
        else:
            return half*half*x