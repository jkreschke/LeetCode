class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        O(n) time, O(max(n,m)) space, where m is the size of the character set
        '''
        seen = OrderedDict()
        for i in range(len(s)):
            seen[s[i]] = i if s[i] not in seen else -1
        for x in seen.keys():
            if seen[x] != -1:
                return seen[x]
        return -1
        
        
