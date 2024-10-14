class Solution:
    def minimumTime(self, power: List[int]) -> int:


        n = len(power)
        @cache
        def dp(used):

            available = []
            for i in range(n):
                if (used>>i)&1 == 1:
                    #already used
                    continue
                available.append(i)

            if not available:
                return 0
            
            g = n-len(available) + 1
            ans = 1e15
            for i in available:
                can = ceil(power[i]/g) + dp(used^(1<<i))
                ans = min(ans, can)
            return ans
        return dp(0)