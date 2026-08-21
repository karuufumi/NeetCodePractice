class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       t = {}
       for i in range(len(nums)):
        if target - nums[i] in t:
            return [t[target-nums[i]],i]
        t[nums[i]] = i