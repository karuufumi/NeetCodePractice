class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        def dfs(n):
            if n >= len(nums):
                res.append(tmp[:])
                return
            tmp.append(nums[n])
            dfs(n+1)
            tmp.pop()
            dfs(n+1)

        dfs(0)
        return res
