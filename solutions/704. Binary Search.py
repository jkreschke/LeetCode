class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Standard O(log(n)) time, O(1) space binary search of sorted array
        '''
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1
            
        
