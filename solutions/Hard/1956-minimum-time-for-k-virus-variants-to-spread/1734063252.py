class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:

        n = len(points)


        def check(t):

            for x in range(101):
                for y in range(101):
                    cnt = 0
                    for j in range(n):
                        x2,y2 = points[j]
                        if abs(x2 - x) + abs(y2-y) <= t:
                            cnt+=1
                    if cnt >= k:
                        return True

        
        l = 0
        r = 401

        #FFFFFTTTTTT
        while l <= r:

            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid +1
        return l