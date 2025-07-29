class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        B = sorted(list(set(B)))
        m,n = len(A), len(B)

        INF = 10**9

        @cache
        def dp(i, last):
            if i == m:
                return 0
            a = b = INF
            if A[i] > last:
                a = dp(i+1, A[i])
            
            j = bisect_right(B, last)
            if j < n:
                b = dp(i+1, B[j]) + 1
            return min(a,b)
        res = dp(0,-1)
        dp.cache_clear()
        return res if res < INF else -1