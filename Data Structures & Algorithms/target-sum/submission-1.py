class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, currentSum):
            if i == len(nums):
                return 1 if currentSum == target else 0

            if (i, currentSum) in memo:
                return memo[(i, currentSum)]

            positive = dp(i + 1, currentSum + nums[i])
            negative = dp(i + 1, currentSum - nums[i])

            memo[(i, currentSum)] = positive + negative
            return memo[(i, currentSum)]

        return dp(0, 0)