class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:

        C = Counter()
        n = len(points)

        def check(can_points):
            a,b,c,d = can_points

            good = (a[1] - c[1] == b[1] - d[1])
            if (a[0] != c[0]) or (b[0] != d[0]):
                return -1
            if (a[1] != b[1]) or (c[1] != d[1]):
                return -1
            exes = [x for (x,y) in (a,b,c,d)]
            ys = [y for (x,y) in (a,b,c,d)]
            low_x = min(exes)
            high_x = max(exes)
            low_y = min(ys)
            high_y = max(ys)

            for i in range(n):
                if points[i] in [a,b,c,d]:
                    continue
                x,y = points[i]
                if low_x <= x <= high_x and low_y <= y <= high_y:
                    #inside box proper
                    return -1

            
            res = (high_x - low_x)*(high_y - low_y)
            return res
                    

        ans = -1
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        a,b,c,d = points[i],points[j],points[k],points[l]
                        if a == b or a == c or a == d or b == c or b == d or c == d:
                            continue
                        ans = max(check([a,b,c,d]), ans)
        return ans