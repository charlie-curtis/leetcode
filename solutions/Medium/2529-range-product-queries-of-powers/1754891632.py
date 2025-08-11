class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        out=[]

        P=[]
        for i in range(32):
            v=1<<i
            if v&n:
                P.append(v)

        for l,r in queries:
            t=1
            for i in range(l,r+1):
                t*=P[i]
                t%=(10**9+7)
            out.append(t)
        return out
                
        