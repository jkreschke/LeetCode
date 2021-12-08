class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        O(n + m) time, where n,m are the lengths of the input strings.
        O(max(n+m,26)) space
        '''
        if len(ransomNote) > len(magazine): return False
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for x in ransomNote.keys():
            if x not in magazine or magazine[x] < ransomNote[x]: return False
        return True
        
        
