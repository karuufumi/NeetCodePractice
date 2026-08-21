class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashTB = set(nums)
        maxCnt = 0
        for i in nums:
            if i-1 in hashTB:
                continue
            curr = i
            cnt = 1
            while curr +1 in hashTB:
                curr = curr +1
                cnt = cnt+1
            maxCnt = max(maxCnt, cnt)
        return maxCnt