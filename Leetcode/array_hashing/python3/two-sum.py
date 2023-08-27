from itertools import combinations
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]


# improved solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
