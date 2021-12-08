class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        O(n) time, O(n) space
        '''
        counts = Counter(nums)
        prev_num = -1
        take = leave = 0        # score by deleting/ leaving current number.
                                # max score possible at current num is max(take,leave)
        for x in sorted(counts):
            if x == prev_num + 1:
                take, leave = leave + x*counts[x], max(take, leave)
            else:
                take, leave = max(take,leave) + x*counts[x], max(take,leave)
            prev_num = x
        return max(take,leave)
            
        
            
