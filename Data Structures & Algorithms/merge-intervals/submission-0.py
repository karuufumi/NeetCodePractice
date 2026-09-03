class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_ = sorted(intervals)

        i = 0
        while i < len(sorted_) - 1:
            if sorted_[i][1] >= sorted_[i + 1][0]:
                sorted_[i][0] = min(sorted_[i][0], sorted_[i + 1][0])
                sorted_[i][1] = max(sorted_[i][1], sorted_[i + 1][1])
                sorted_.pop(i + 1)
            else:
                i += 1

        return sorted_