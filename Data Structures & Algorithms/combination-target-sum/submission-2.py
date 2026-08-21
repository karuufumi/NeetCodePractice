class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[] 
        tmp=[]
        def dfs(i,sum_):
            if sum_ == target:
                res.append(tmp[::])
                return
            if sum_ > target:
                return
        
            for j in range(i,len(nums)):
                sum_ = sum_ + nums[j]
                tmp.append(nums[j])
                dfs(j, sum_)
                sum_ -= nums[j]
                tmp.pop()
        dfs(0,0)
        return res