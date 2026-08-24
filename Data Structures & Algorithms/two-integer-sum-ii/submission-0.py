class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return []
        i,j,res =0, len(nums)-1,[]
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
                continue
            elif nums[i] + nums[j] < target:
                i +=1
                continue
            else:
                res.append(i+1)
                res.append(j+1)
                break
                #return res
        return res