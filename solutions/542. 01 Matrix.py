class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        DP solution. O(nm) time, O(nm) space
        '''
        m, n = len(mat), len(mat[0])
        dist = [[float('inf')]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: dist[i][j] = 0
                if mat[i][j] != 0:
                    if i > 0: dist[i][j] = 1 + dist[i-1][j]
                    if j > 0: dist[i][j] = min(dist[i][j], 1 + dist[i][j-1])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j] != 0:
                    if i + 1 < m: dist[i][j] = min(dist[i][j],1 + dist[i+1][j])
                    if j + 1 < n: dist[i][j] = min(dist[i][j],1 + dist[i][j+1])
        return dist
                
                        
                    
                
                
        
