class Solution:
    def minDays(self, nums: List[int], m: int, k: int) -> int:



        INF = 10**10
        l = 0
        r = INF

        n = len(nums)
        def check(t):
            tmp = [1 if x <= t else 0 for x in nums]
            seen = 0
            for c, g in groupby(tmp):
                if c == 0:
                    continue
                l = len(list(g))
                seen+=l//k
            return seen >= m

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1

        return l if l<=INF else -1
        