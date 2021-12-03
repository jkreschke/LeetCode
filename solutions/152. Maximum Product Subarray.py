class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = mx = mn = nums[0]
        for x in nums[1:]:
            mx, mn = max(mx*x, mn*x, x), min(mx*x, mn*x, x)
            ans = max(ans, mx)
        return ans
    
        '''
        dp solution, time complexity O(n^2), time limit exceeded.
        '''
        ans, dp = nums[0], [nums[0]]
        for x in nums[1:]:
            for j in range(len(dp)):
                dp[j] *= x
                dp.append(x)
            ans = max(ans,*dp)
        return ans
            
            
        
        
