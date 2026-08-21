class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTB = set()
        for i in nums:
            if i in hashTB:
                return True
            else:
                hashTB.add(i)
        return False