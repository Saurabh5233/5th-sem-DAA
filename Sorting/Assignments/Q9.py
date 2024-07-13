# https://leetcode.com/problems/relative-ranks/description/

# Relative Ranks

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a list of tuples (score, index)
        score_with_index = [(s, i) for i, s in enumerate(score)]
        
        # Sort the list by score in descending order
        score_with_index.sort(reverse=True, key=lambda x: x[0])
        
        # Prepare the result array with the same length as score
        result = [""] * len(score)
        
        # Define the top three ranks
        top_ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        # Assign ranks based on sorted order
        for rank, (s, i) in enumerate(score_with_index):
            if rank < 3:
                result[i] = top_ranks[rank]
            else:
                result[i] = str(rank + 1)
        
        return result