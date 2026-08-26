class Solution:
    def qSort(self, intervals: List[Interval]):
        def hoarePartition(arr, low, high):
            pivot = arr[(low + high) // 2].start

            i = low - 1
            j = high + 1

            while True:
                i += 1
                while arr[i].start < pivot:
                    i += 1

                j -= 1
                while arr[j].start > pivot:
                    j -= 1

                if i >= j:
                    return j

                arr[i], arr[j] = arr[j], arr[i]

        def quickSort(arr, low, high):
            if low < high:
                p = hoarePartition(arr, low, high)
                quickSort(arr, low, p)
                quickSort(arr, p + 1, high)

        quickSort(intervals, 0, len(intervals) - 1)

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        self.qSort(intervals)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True