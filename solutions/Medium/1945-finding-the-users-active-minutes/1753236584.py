class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        d = defaultdict(set)

        for id, t in logs:
            d[id].add(t)
        
        C = Counter()
        for v in d.values():
            C[len(v)]+=1
        
        out = []
        for i in range(1,k+1):
            out.append(C[i])
        return out
        