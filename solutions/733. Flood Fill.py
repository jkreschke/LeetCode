class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''
        DFS. O(mn) time, O(mn) space
        '''
        oldColor = image[sr][sc]
        if oldColor == newColor: return image
        m = len(image)
        n = len(image[0])
        def DFS(i,j):
            if image[i][j] == oldColor:
                image[i][j] = newColor
                if i > 0: DFS(i-1,j)
                if j > 0: DFS(i,j-1)
                if i < m - 1: DFS(i+1,j)
                if j < n - 1: DFS(i,j+1)
                    
        DFS(sr,sc)
        return image
            
        
