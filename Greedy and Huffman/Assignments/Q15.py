# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

# Job Sequencing Problem


from typing import List, Tuple
import heapq

class Job:
    def __init__(self, job_id: int, deadline: int, profit: int):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def JobScheduling(self, jobs: List[Job], n: int) -> List[int]:
        # Sort jobs by their profit in descending order
        jobs.sort(key=lambda x: x.profit, reverse=True)
        
        max_deadline = max(job.deadline for job in jobs)
        slots = [False] * (max_deadline + 1)  # Track used slots
        max_profit = 0
        count_jobs = 0
        
        for job in jobs:
            # Find a free slot for this job (from its deadline to 0)
            for j in range(job.deadline, 0, -1):
                if not slots[j]:
                    slots[j] = True
                    max_profit += job.profit
                    count_jobs += 1
                    break
        
        return [count_jobs, max_profit]

# Example usage:
jobs = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 1, 40), Job(4, 1, 30)]
sol = Solution()
result = sol.JobScheduling(jobs, len(jobs))
print(result)  # Output: [2, 60]
