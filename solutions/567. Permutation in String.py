class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Using counters. O(n) time, where n is length of s2. O(m) space,
        where m is the size of the character set.
        '''
        if len(s1) > len(s2): return False
        counts, window_counts = Counter(s1), Counter(s2[:len(s1)])
        if counts == window_counts: return True
        for i in range(len(s1),len(s2)):
            if s2[i] in window_counts:
                window_counts[s2[i]] += 1
            else:
                window_counts[s2[i]] = 1
            window_counts[s2[i - len(s1)]] -= 1
            if window_counts[s2[i-len(s1)]] == 0:
                del window_counts[s2[i-len(s1)]]
            if counts == window_counts: return True
        return False
                
            
