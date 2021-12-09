class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Second attempt. Try to do better on space complexity.
        O(n) time, O(1) space
        '''
        jumps = 0
        farthest = 0
        prev = 0
        for i in range(len(nums)):
            if i > prev:
                jumps += 1
                prev = farthest
            farthest = max(farthest, i + nums[i])
        return jumps
            
        
        '''
        BFS. O(n) time, O(n) space
        '''
        if len(nums) == 1: return 0
        
        farthest = 0
        queue = collections.deque([(0,0)])
        while queue:
            cur,steps = queue.popleft()
            for j in range(farthest + 1,cur + nums[cur] + 1):
                if j >= len(nums) - 1: return steps + 1
                queue.append((j, steps + 1))
            farthest = max(farthest, cur + nums[cur])
