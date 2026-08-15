import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.dataArry = nums[:]
        self.k = k

        heapq.heapify(self.dataArry)

        while(len(self.dataArry) > self.k):
            heapq.heappop(self.dataArry)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.dataArry,val)
        
        if len(self.dataArry) > self.k:
            heapq.heappop(self.dataArry)
            
        return heapq.nsmallest(1, self.dataArry)[0]