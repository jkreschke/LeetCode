class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        O(N) time, O(N) space solution
        '''
        stack = []
        for dig in num:
            while k > 0 and stack and stack[-1] > dig:
                stack.pop()
                k -= 1
            stack.append(dig)
        while k > 0:
            stack.pop()
            k -= 1
        ans = (''.join(stack)).lstrip('0')
        return ans if ans else '0'
                
        '''
        O(N^2) time, O(1) space soln, where N = len(num)
        write a helper function to remove one digit at a time
        '''
        def helper(s):
            if len(s) == 1: return '0'
            i = 0
            while i < len(s) - 1:
                if s[i] > s[i+1]:
                    break
                i += 1
            s = s[:i] + s[i+1:]
            if i == 0: s = s.lstrip('0')
            return s if s else '0'
        for _ in range(k):
            num = helper(num)
            if num == '0': break
        return num
        
