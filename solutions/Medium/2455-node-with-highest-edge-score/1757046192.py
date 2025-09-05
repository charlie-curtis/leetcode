class Solution:
    def edgeScore(self, edges: List[int]) -> int:


        C = Counter()
        for f,to in enumerate(edges):
            C[to]+=f
        
        mx = max(C.values())
        for i in range(len(edges)):
            if C[i] == mx:
                return i
        