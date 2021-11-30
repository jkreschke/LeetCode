class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        O(MN) time, O(MN) space
        '''
        rowd = defaultdict(set)
        cold = defaultdict(set)
        boxd = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    k = (i // 3) * 3 + (j // 3)
                    cur = board[i][j]
                    if cur in rowd[i]: return False
                    if cur in cold[j]: return False
                    if cur in boxd[k]: return False
                    rowd[i].add(cur)
                    cold[j].add(cur)
                    boxd[k].add(cur)
        return True
​
        
