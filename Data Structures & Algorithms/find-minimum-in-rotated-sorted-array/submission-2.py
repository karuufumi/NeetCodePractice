class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)
        
        while l < r:
            m = (l+r-1)//2
            if nums[m] > nums[r-1]:
                l = m+1
            else:
                r = m
                
            if nums[m] <= nums[l] and nums[m] <= nums[r-1]: 
                return nums[m]