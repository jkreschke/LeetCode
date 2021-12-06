class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        return ' '.join([y[::-1] for y in x])
        
