class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robbery(ls):
            n = len(ls)
            dp = [0] * (n + 1)
            dp[1] = ls[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 2] + ls[i - 1], dp[i - 1])
            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        
        return(max( robbery(nums[1:]),robbery(nums[:-1])))
        