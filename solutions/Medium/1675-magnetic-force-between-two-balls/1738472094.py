class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:


        pos.sort()
        def check(t):
            prev= -1e15
            used = 0
            for x in pos:
                if x-prev>=t:
                    prev = x
                    used+=1
            return used >= m


        l = 0
        r = 10**9+1

        while l<=r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid -1
        return r
        