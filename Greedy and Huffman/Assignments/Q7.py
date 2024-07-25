# https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

# Chocolate Distribution Problem


class Solution:

    def findMinDiff(self, A,N,M):

        if N<M:
            return -1
        A.sort()
        i=0
        j = M-1
        min_diff = float('inf')
        
        while(j<N):
            if(min_diff> A[j]-A[i]):
                min_diff = A[j]-A[i]
            i+=1
            j+=1
        
        return min_diff
