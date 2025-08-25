class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:


        ans = 0
        C = Counter()
        for i,(x,y) in enumerate(points):
            for j, (x1,y1) in enumerate(points):
                if i == j:
                    continue
                d1 = sqrt((x1-x)**2 + (y1-y)**2)
                ans+=C[(i,d1)]
                C[(i,d1)]+=1
        return ans*2
                    
        