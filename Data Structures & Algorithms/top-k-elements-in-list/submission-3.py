class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {num : 0 for num in nums}
        for i in range(len(nums)):
            bucket[nums[i]] +=1
        lst = [[] for _ in range(len(nums) + 1)]
        for i,j in bucket.items():
            lst[j].append(i)
        res=[]

        for freq in range(len(lst) - 1, 0, -1):
            for num in lst[freq]:
                # add num to res
                res.append(num)
                if len(res) ==k:
                    return res