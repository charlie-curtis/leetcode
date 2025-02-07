class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:


        d = {}
        C = Counter()
        out = []
        for x, color in queries:
            if x in d:
                cur = d[x]
                C[cur]-=1
                if C[cur] == 0:
                    del C[cur]
            d[x] = color
            C[color]+=1
            out.append(len(C.keys()))
        return out
