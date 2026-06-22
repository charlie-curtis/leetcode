class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:

        H={}
        for x,y,r in circles:
            if (x,y) not in H:
                H[(x,y)] = 0
            H[(x,y)] = max(H[(x,y)], r)
        circles=[]
        for (x,y),r in H.items():
            circles.append([x,y,r])

        pts=set()
        def check(x,y,x1,y1,r):
           return sqrt(abs(x1-x)**2 + abs(y1-y)**2) <= r
        for x,y,r in circles:
            for x1 in range(x-r,x+r+1):
                for y1 in range(y-r,y+r+1):
                    if check(x,y,x1,y1,r):
                        pts.add((x1,y1))
        return len(pts)