class Solution:
    memo = {1:[1], 2:[1,1]}
    def generate(self, numRows: int) -> List[List[int]]:
        
        def helper(n):
            if n in self.memo:
                return self.memo[n]
            else:
                prev = helper(n-1)
                x = [1]
                for j in range(len(prev) - 1):
                    x.append(prev[j] + prev[j+1])
                x.append(1)
                self.memo[n] = x
                return x
        
        return [helper(n+1) for n in range(numRows)]
            
        
