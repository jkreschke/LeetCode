class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Standard binary search, O(n) time, O(1) space.
        If target is not found do one extra check to see where it should
        be placed
        '''
        if target < nums[0]: return 0
        if target > nums[-1]: return len(nums)
        
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
                
        if nums[i] < target:
            return i + 1
        else:
            return i
        
        
