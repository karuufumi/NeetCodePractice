class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            prevMax = curMax
            prevMin = curMin

            curMax = max(
                x,
                x * prevMax,
                x * prevMin
            )

            curMin = min(
                x,
                x * prevMax,
                x * prevMin
            )

            res = max(res, curMax)

        return res