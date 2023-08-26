from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True


#
# 470 ms
# 30.9 MB

## Improved solution
# class Solution:
#    def containsDuplicate(self, nums: List[int]) -> bool:
#        seen = set()
#        for num in nums:
#            if num in seen:
#                return True
#            seen.add(num)
#        return False
