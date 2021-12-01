class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedy approach. O(nlog(n)) time complexity. O(1) space.
        min#(intervals to remove) = len(intervals) - max#(disjoint intervals)
        '''
        intervals.sort()
        end = intervals[0][1]
        count = 1
        for interval in intervals[1:]:
            if end <= interval[0]:
                count += 1
                end = interval[1]
            else:
                if end > interval[1]:
                    end = interval[1]
        return len(intervals) - count
        
