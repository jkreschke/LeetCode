class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        Two pointer. O(n) time complexity
        '''
        i,j = 0,len(nums)-1
        nums = [x**2 for x in nums]
        out = []
        while i <= j:
            if nums[i] < nums[j]:
                out.append(nums[j])
                j -= 1
            else:
                out.append(nums[i])
                i += 1
        return out[::-1]
                
        
