class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Shellsort

        def swap(nums, n1, n2):
            nums[n1], nums[n2] = nums[n2], nums[n1]

        def insSort(nums, n, incr):
            i = incr

            while i < n:
                j = i

                while j >= incr and nums[j] < nums[j - incr]:
                    #swap(nums, j, j - incr)
                    nums[j],nums[j-incr] = nums[j-incr],nums[j]
                    j -= incr

                i += 1

        n = len(nums)
        gap = n // 2

        while gap > 0:
            insSort(nums, n, gap)
            gap //= 2

        return nums