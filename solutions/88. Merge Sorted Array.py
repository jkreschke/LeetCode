class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Three pointer solution. O(n+m) time, O(1) space
        Third pointer is to keep track of where element should be placed
        """
        i, j, k = m - 1, n - 1, n + m - 1
        while k >= 0:
            left = (j ==-1 or (i>=0 and j>=0 and nums1[i] >= nums2[j]))
            if left:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -=1
                
            
        
        
