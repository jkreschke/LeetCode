class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Solution using Hash table. O(N) time complexity,
        O(N) space complexity
        '''
        d = dict()
        ans = 0
        for x in nums:
            if x in d:
                continue
            else:
                d[x] = None
                right = 0 if x + 1 not in d else d[x + 1]
                left = 0 if x - 1 not in d else d[x - 1]
                curLen = right + left + 1
                d[x + right] = d[x - left] = curLen
                ans = max(ans, curLen)
        return ans
                
        
