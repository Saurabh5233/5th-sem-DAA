# https://leetcode.com/problems/lemonade-change/description/

# Lemonade Change

class Solution(object):
    def lemonadeChange(self, bills):
          """
          :type bills: List[int]
          :rtype: bool
          """
          if bills[0]!= 5:
            return False
          
          fives, tens =0,0

          for bill in bills:
            if bill == 5:
              # keep the money
              fives+= 1
            elif bill == 10:
              if fives>=1:
                #Give one $5 note
                fives -=1
                tens +=1
              else:
                return False
            else:
              # in case we got a $20 note...
              #check if we have atleast one $10 note and one$5 note
              if tens>=1 and fives>=1:
                tens-=1
                fives-=1
               
              # otherwise check we have 3 $5 notes
              elif fives >=3:
                fives -=3
              else:
                return False
          return True

        