class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n - 1)
            ans = ''
            count = 1
            for i in range(1,len(prev)):
                if prev[i] == prev[i-1]:
                    count += 1
                else:
                    ans += str(count) + prev[i-1]
                    count = 1
            ans += str(count) + prev[-1]
            return ans
                    
                
        
