from typing import List

def counting_sort(nums: List[int]) -> List[int]:
    N = len(nums)
    if N == 0:
        return []

    max_element = max(nums)
    k = max_element + 1

    # Initialize and populate the frequency array
    count = [0] * k
    for x in nums:
        count[x] += 1

    # Reconstruct the sorted array
    sorted_nums = []
    for i in range(k):
        sorted_nums.extend([i] * count[i])

    return sorted_nums


nums = [2,0,3,0,1,1,5,3,11]
print(counting_sort(nums))

