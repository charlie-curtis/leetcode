class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:


        sd = SortedDict()
        C = Counter()
        d = defaultdict(int)

        for start,end,h in buildings:
            d[start]+=h
            d[end]-=h
            C[start]+=1
            C[end]-=1


        events = sorted(C.keys())
        n = len(events)
        segs = []
        curh = curcnt = 0
        for i in range(n-1):
            start = events[i]
            end = events[i+1]
            curcnt+=C[start]
            curh+=d[start]
            if curcnt != 0:
                segs.append([start,end, curh//curcnt])
            
        
        out = []
        for start,end, h in segs:
            if not out or out[-1][2] != h or out[-1][1] < start:
                out.append([start,end,h])
            else:
                out[-1][1] = end
        return out






