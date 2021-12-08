class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        O(n) time, O(n) space
        '''
        if len(nums) <= 3:
            return max(nums)
        nums2 = nums[1:].copy() # if first house is skipped
        nums.pop()
        nums[2] += nums[0]
        nums2[2] += nums2[0]
        for i in range(3,len(nums)):
            nums[i] += max(nums[i-2],nums[i-3])
            nums2[i] += max(nums2[i-2],nums2[i-3])
        return max(nums[-2:] + nums2[-2:])
        
