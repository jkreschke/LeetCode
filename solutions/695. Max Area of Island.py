class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        DFS. O(nm) time, O(mn) space in implicit call stack
        '''
        m, n = len(grid), len(grid[0])
        
        def DFS(x,y):
            if grid[x][y] == 1:
                grid[x][y] = 0
                self.area += 1
                if x < m - 1: DFS(x+1,y)
                if x > 0: DFS(x-1,y)
                if y < n - 1: DFS(x,y+1)
                if y > 0: DFS(x,y-1)
        max_area = 0
        self.area = 0
        
        for i in range(m):
            for j in range(n):
                DFS(i,j)
                max_area = max(max_area,self.area)
                self.area = 0
        return max_area
        
