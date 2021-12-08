class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        O(N) time, O(M) space, M = size of character set
        '''
        seen = dict()
        j = 0 
        ans = 0
        for i in range(0,len(s)):
            if s[i] not in seen:
                ans = max(ans, i - j + 1)
            else:
                target = seen[s[i]]
                while j <= target:
                    if s[j] in seen:
                        del seen[s[j]]
                    j += 1
            seen[s[i]] = i
        return ans
                
        
