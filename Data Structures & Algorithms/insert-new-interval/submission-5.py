class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # Find insertion position
        left, right = 0, len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)

        # Merge in-place
        intervals.insert(left, newInterval)

        start =  max(0,left - 1)
        
        write = start

        for read in range(start + 1, len(intervals)):
            current = intervals[write]
            nxt = intervals[read]

            if nxt[0] <= current[1]:
                current[1] = max(current[1], nxt[1])
            else:
                write += 1
                intervals[write] = nxt

        del intervals[write + 1:]
        return intervals