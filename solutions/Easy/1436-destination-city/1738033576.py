class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        out = Counter()
        for u,v in paths:
            out[u]+=1
            out[v]+=0

        for k,v in out.items():
            if v == 0:
                return k
        