class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        i = 0
        while i < len(nums):
            if maxJump >= i:
                maxJump = max(maxJump, i + nums[i])
            i+=1
        return True if maxJump >= len(nums)-1 else False