# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

# N meetings in one room


class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,N,start,end):
        if N<=1:
            return N
          
        meetings = [[start[i], end[i]] for i in range(N)]
        meetings.sort(key = lambda x:x[1])
        current_end = meetings[0][1]
      
        max_count = 1
        for i in range(1,N):
            if meetings[i][0] > current_end:
              max_count+=1
              current_end = meetings[i][1]
          
        return max_count
        