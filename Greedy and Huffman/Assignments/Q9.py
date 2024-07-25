# https://leetcode.com/problems/assign-cookies/description/

# Assign Cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        i,j =0,0
        g.sort()
        s.sort()
        count=0

        while i < n and j<m:
            if g[i] <= s[j]:
                count+=1
                i+=1
            j+=1
        return count