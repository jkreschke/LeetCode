class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Simple dp soln. O(n) time & space
        '''
        dp = [0,0]
        for i in range(2,len(cost)+1):
            dp.append(min(cost[i-2]+dp[-2], cost[i-1]+dp[-1]))
        return dp[-1]
             
        
        
