class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = []
        modified_list = []

        for num in nums:
            if num == val:
                k.append(num)
            else:
                modified_list.append(num)
        
        for i in range(len(nums)):
            if len(modified_list) < len(nums):
                nums.pop()
                print('if' + str(nums))
        
        for i in range(len(nums)):
            nums[i] = modified_list[i]

        return len(nums)
        