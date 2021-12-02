class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        O(N) time, O(N) space
        '''
        seen = defaultdict(int)
        for i in range(10,len(s)+1):
            seen[s[i-10:i]] += 1
        return [x for x in seen if seen[x] > 1]
            
        
