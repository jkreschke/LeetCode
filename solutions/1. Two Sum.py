class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Hashing. O(n) time complexity, O(n) space complexity
        
        One might try to obtain an O(1) space algorithm by sorting first,
        but this will still require O(n) space in order to map back to the
        original indices!
        '''
        seen = dict()
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [i, seen[target - nums[i]]]
            else:
                seen[nums[i]] = i
        
​
        
​
        
