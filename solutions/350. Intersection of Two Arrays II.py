class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Hashing with Counter. Iterate through intersection of the keys.
        O(n) time, O(n) space
        '''
        nums1, nums2, ans = Counter(nums1), Counter(nums2), []
        for k in set(nums1.keys()) & set(nums2.keys()):
            ans += [k]*min(nums1[k],nums2[k])
        return ans
