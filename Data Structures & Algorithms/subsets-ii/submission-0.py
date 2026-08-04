from typing import List
from functools import reduce

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        def dfs(begin: int, out: List[int]) -> List[List[int]]:

            candidates = [
                i for i in range(begin, len(nums))
                if i == begin or nums[i] != nums[i - 1]
            ]
            branches = (dfs(i + 1, out + [nums[i]]) for i in candidates)
            return [out] + reduce(lambda acc, b: acc + b, branches, [])

        return dfs(0, [])
