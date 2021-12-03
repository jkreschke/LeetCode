# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
​
class Solution:
    '''
    Standard binary search. O(log(n)) time, O(1) space
    '''
    def firstBadVersion(self, n):
        i, j = 1, n
        while i < j:
            mid = (i+j)//2
            if isBadVersion(mid):
                j = mid
            else:
                i = mid + 1
        return i
        
