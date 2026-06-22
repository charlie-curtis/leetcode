class Solution:
    def countRoutes(self, locs: List[int], start: int, finish: int, fuel: int) -> int:


        MOD = 10**9 + 7
        @cache
        def dp(cur, f, t):

            if f < 0:
                return 0
            ans = 0
            if cur == t:
                ans+=1


            for i,x in enumerate(locs):
                if cur == i:
                    continue
                ans+=dp(i, f- abs(locs[cur]-x), t)
                ans%=MOD
            return ans

        return dp(start, fuel, finish)