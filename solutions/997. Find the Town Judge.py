class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic = defaultdict(set)
        for vec in trust: # dic[i] contains j if i trusts j
            dic[vec[0]].add(vec[1])
        for i in range(1,n+1):
            if len(dic[i]) == 0: # i trusts nobody, may be the judge
                if all(i in dic[j] for j in set(range(1,n+1))-{i}):
                    return i
        return -1
                
        
