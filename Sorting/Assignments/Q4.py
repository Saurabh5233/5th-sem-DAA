# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

# average-salary-excluding-the-minimum-and-maximum-salary


class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        n = len(salary)
        newSalary = self.bubble_sort(salary)
        totalSalary= sum(newSalary)
        # sum =0
        # for i in newSalary:
        #     sum+=i

        average = (totalSalary -(newSalary[0]+newSalary[n-1]))/float(n-2)
        return average
    
    def bubble_sort(self,salary):
        n = len(salary)
        for i in range(0,n):
            flag = False
            for j in range(0,n-i-1):
                if salary[j]> salary[j+1]:
                    flag = True
                    salary[j],salary[j+1] = salary[j+1], salary[j]
                    
            if(flag == False):
                break

        return salary
    
    
    
# without sorting::::

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        minSal = salary[0]
        maxSal = salary[0]
        
        for i in salary:
            if i < minSal:
                minSal = i
            if i > maxSal:
                maxSal = i 

        totalSalary = sum(salary)
        avg = (totalSalary - minSal - maxSal) / float(len(salary) - 2)
        return avg

