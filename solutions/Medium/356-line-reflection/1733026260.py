class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:

        d = defaultdict(list)

        points = set([(x,y) for x,y in points])
        INF = float('inf')
        for x,y in points:
            d[y].append(x)


        def find(yVal):

            pts = sorted(d[yVal])
            n = len(pts)

            i = 0
            j = n-1
            seen = set()
            while i <= j:
                seen.add((pts[i] + pts[j]) / 2)
                i+=1
                j-=1

            if len(seen) != 1:
                return INF
            else:
                return list(seen)[0]


        seen = set()
        for y in d.keys():
            seen.add(find(y))
        
        if INF in seen or len(seen) != 1:
            return False
        return True
                
        