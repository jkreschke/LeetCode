class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        modify nums so that nums[i] = max amount that can be made by robbing house i.
        O(n) time, O(1) space.
        '''
        if len(nums) <= 2:
            return max(nums)
        nums[2] = nums[2]+nums[0]
        for i in range(3,len(nums)):
            nums[i] += max(nums[i-2],nums[i-3])
        return max(nums[-2:])
    
        
