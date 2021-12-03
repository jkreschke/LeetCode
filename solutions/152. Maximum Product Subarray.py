class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Second attempt dp, O(n) time complexity, O(1) space complexity.
        Store the ans, and maximum, minimum product that uses previous number
        '''
        ans = mx = mn = nums[0]
        for x in nums[1:]:
            mx, mn = max(mx*x, mn*x, x), min(mx*x, mn*x, x)
            ans = max(ans, mx)
        return ans
    
        '''
        first attempt
        dp solution, time complexity O(n^2), time limit exceeded.
        space complexity O(n)
        '''
        ans, dp = nums[0], [nums[0]]
        for x in nums[1:]:
            for j in range(len(dp)):
                dp[j] *= x
                dp.append(x)
            ans = max(ans,*dp)
        return ans
            
            
        
        
