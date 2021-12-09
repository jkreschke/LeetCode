class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        O(n) time, O(1) space.
        '''
        jump = 1
        for x in nums:
            if jump == 0:
                return False
            jump = max(x, jump - 1)
        return True
            
                
                
            
            
            
            
        
