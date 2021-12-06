class Solution:
    def tribonacci(self, n: int, memo = {0:0,1:1,2:1}) -> int:
        '''
        Recursion plus memoization. O(n) time, O(n) space
        '''
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
            return memo[n]
        
