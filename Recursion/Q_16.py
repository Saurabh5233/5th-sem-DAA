# power of four

class Solution(object):
    def isPowerOffour(self, n) :
        if(n<=0):
            return False
        
        if(n==1):
            return True
        
        if(n%4 !=0):
            return False
        
        return self.isPowerOffour(n/4)
        