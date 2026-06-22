class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        l = 0
        r = 10**7

        def check(mid):
            if mid == 0:
                return False
            t = 0
            for i,x in enumerate(dist):
                if i == len(dist)-1:
                    t+=x/mid
                else:
                    t+=((x+mid-1)//mid)
            return t <= hour



        #FFFFTTTTT
        while l<=r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        

        return l if l <= 10**7 else -1
        