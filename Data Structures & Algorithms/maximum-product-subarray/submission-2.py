class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memoMax = [0] * len(nums)
        memoMin = [0] * len(nums)
        memoMax[0] = nums[0]
        memoMin[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            a = nums[i]
            b = nums[i] * memoMax[i - 1]
            c = nums[i] * memoMin[i - 1]

            memoMax[i] = max(a, b, c)
            memoMin[i] = min(a, b, c)

            res = max(res, memoMax[i])

        return res