class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:

        n = len(bottomLeft)

        def check(i,j):
            bl1 = bottomLeft[i]
            tr1 = topRight[i]
            
            bl2 = bottomLeft[j]
            tr2 = topRight[j]

            x1,y1,x2,y2 = bl1[0], bl1[1], tr1[0], tr1[1]
            x3,y3,x4,y4 = bl2[0], bl2[1], tr2[0], tr2[1]

            x_overlap = max(0,min(x2,x4) - max(x1,x3))
            y_overlap = max(0,min(y2,y4) - max(y1,y3))

            return min(x_overlap, y_overlap)**2



        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                ans = max(ans, check(i,j))
        return ans

        