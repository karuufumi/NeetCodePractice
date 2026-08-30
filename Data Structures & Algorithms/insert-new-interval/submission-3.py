class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals ) ==0:
            return [newInterval]
        i = 0
        j = len(intervals)-1
        ### BINARY SEARCH
        while i <=j:
            mid = (i+j)//2
            if newInterval[0] < intervals[mid][0]:
                j = mid-1
            else:
                i = mid+1
        intervals.insert(i,newInterval)
        write = 0

        for read in range(1, len(intervals)):
            current = intervals[write]
            next_interval = intervals[read]

            if next_interval[0] <= current[1]:
                current[1] = max(current[1], next_interval[1])
            else:
                write += 1
                intervals[write] = next_interval

        del intervals[write + 1:]
        return intervals

