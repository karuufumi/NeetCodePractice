import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #ignore the root since it does not affect solution
        distances = [((x**2 + y**2), [x, y]) for x, y in points]
        heapq.heapify(distances)
        res = []
        for i in range(k):
            _,point = heapq.heappop(distances)
            res.append(point)
        return res