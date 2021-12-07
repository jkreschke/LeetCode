class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        O(n) time, O(n) space
        '''
        dp = [1,2]
        if n <= 2:
            return dp[n-1]
        for _ in range(2,n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
