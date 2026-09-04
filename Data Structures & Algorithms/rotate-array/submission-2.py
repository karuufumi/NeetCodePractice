class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        count = 0
        start = 0

        while count < n:
            current = start
            carry = nums[current]

            while True:
                nxt = (current + k) % n

                nums[nxt], carry = carry, nums[nxt]

                current = nxt
                count += 1

                if current == start:
                    break

            start += 1