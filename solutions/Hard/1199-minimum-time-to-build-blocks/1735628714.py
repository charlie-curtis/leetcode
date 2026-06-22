class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:

        blocks.sort(reverse=True)
        n = len(blocks)

        INF = 2*10**6

        @cache
        def dp(b, w):
            if b == n:
                return 0
            if w == 0:
                return INF

            best = INF
            if w < n-b:
                best = min(best, split+dp(b,min(2*w,n-b)))

            m = blocks[b]
            #editorial: To optimize the solution from O(n^3) to O(n^2) notice that if you choose to split, it is always better to split all the workers you have.

            a = max(m, dp(b+1, w-1))
            best = min(best, a)

            return best

        res = dp(0,1)
        dp.cache_clear()
        return res

