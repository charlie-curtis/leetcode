class Solution:
    def removeCoveredIntervals(self, inv: List[List[int]]) -> int:
        
        inv.sort(key=lambda x:(x[0],-x[1]))
        out=[]
        for s,e in inv:
            if not out or out[-1][1] < e:
                out.append([s,e])
        return len(out)
        