class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Use a mapping from array indices to matrix indices. O(log(m*n)) time, O(1) space
        '''
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m * n - 1
        while i <= j:
            mid = (i + j)//2
            row, col = divmod(mid, n) 
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False
