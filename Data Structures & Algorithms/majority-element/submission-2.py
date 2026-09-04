class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0 
        candi = None
        for i in nums:
            if cnt ==0:
                candi = i
                cnt =1
            elif candi == i:
                cnt +=1
            else:
                cnt -=1
        
        return candi
        