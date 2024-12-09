class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        def check(a,b, r):
            return sqrt((a[0] - b[0])**2 + (a[1] -b[1])**2) <= r


        out = []
        for x,y,r in queries:
            cnt = 0
            for a,b in points:
                if check([x,y], [a,b], r):
                    cnt+=1
            out.append(cnt)
        return out
        