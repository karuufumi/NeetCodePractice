class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTB = set()
        for num in nums:
            if num in hashTB:
                return True
            hashTB.add(num)
        return False