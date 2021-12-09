class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        '''
        DFS. O(n) time, O(n) space
        '''
        if arr[start] == 0: return True
        stack = [start]
        visited = set(stack)
        while stack:
            cur = stack.pop()
            for j in [cur - arr[cur], cur + arr[cur]]:
                if 0 <= j < len(arr) and j not in visited:
                    if arr[j] == 0: return True
                    visited.add(j)
                    stack.append(j)
        return False
        
