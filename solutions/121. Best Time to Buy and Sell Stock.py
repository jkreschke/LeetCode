class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        One pass. O(n) time, O(1) space
        '''
        buy, profit = prices[0], 0
        for i in range(1,len(prices)):
            profit = max(profit, prices[i] - buy)
            buy = min(prices[i], buy)
        return profit
        
