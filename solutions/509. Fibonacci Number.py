class Solution:
    def fib(self, n: int, memo = {0:0, 1:1}) -> int:
        '''
        Recursion plus memoization. O(n) time, O(n) space
        '''
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.fib(n-2) + self.fib(n-1)
            return memo[n]
        
