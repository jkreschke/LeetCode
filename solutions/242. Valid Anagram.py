class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        O(n+m) time, O(max(n+m,26)) space
        '''
        return Counter(s) == Counter(t)
