class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:

        d = defaultdict(set)
        for i,li in enumerate(hats):
            for x in li:
                d[x-1].add(i)
        n = len(hats)
        numHats = 40
        MOD = 10**9 + 7
        @cache
        def dp(i, state):
            if state == (2**n)-1:
                return 1
            if i == numHats:
                return 0

            ans = dp(i+1, state)

            for p in d[i]:
                if (1<<p & state) == 0:
                    ans+=dp(i+1, state|(1<<p))
                    ans%=MOD
            return ans
        return dp(0, 0)