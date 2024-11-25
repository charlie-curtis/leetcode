class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:

        n = len(points)

        def get_slope(i,j):
            if points[i][0] == points[j][0]:
                #vertical line
                return 1e15
            return (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
        @cache
        def dp(used):
            available = []
            for i in range(n):
                if used&(1<<i) == 0:
                    available.append(i)
            
            if not available:
                return 0
            if len(available) == 1:
                return 1

            j = available.pop()
            can = 1e15
            for i in available:
                tmp = used|(1<<j)
                slope = get_slope(j,i)
                for k in range(i,n):
                    if get_slope(j,k) == slope:
                        tmp = tmp|(1<<k)

                can = min(can, 1 + dp(tmp))
            return can
        return dp(0)