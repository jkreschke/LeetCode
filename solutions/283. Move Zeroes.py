class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Two pointer solution. O(n) time, O(1) space.
        """
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        if i < len(nums):
            for j in range(i+1,len(nums)):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    i += 1
            for j in range(i, len(nums)):
                nums[j] = 0
        
        
        
