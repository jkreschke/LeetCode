class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Two pointer solution. O(n) time, O(1) space
        '''
        i, j = 0, len(numbers) - 1
        res = numbers[i] + numbers[j]
        while res != target:
            if res < target: i += 1
            else: j -= 1
            res = numbers[i] + numbers[j]
        return [i+1,j+1]
            
