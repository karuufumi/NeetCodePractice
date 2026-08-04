from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums[:]]

        first = nums[0]
        perms_without_first = self.permute(nums[1:])
        res = []
        for perm in perms_without_first:
            for i in range(len(perm) + 1):
                res.append(perm[:i] + [first] + perm[i:])
        return res