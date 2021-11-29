class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Solution using stack. O(N) time, O(N) space
        '''
        left = {'(','{','['}
        right = {')':'(','}':'{',']':'['}
        stack = []
        for sym in s:
            if sym in left:
                stack.append(sym)
            if sym in right:
                if not stack or right[sym] != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0
        
