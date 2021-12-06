class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c: # illegal reshape
            return mat
        
        ans = []
        for i in range(r):
            row = []
            for j in range(c):
                old_row = (c * i + j)//n
                old_col = c * i + j - old_row*n
                row.append(mat[old_row][old_col])
            ans.append(row)
        return ans
