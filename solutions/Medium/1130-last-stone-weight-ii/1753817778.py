class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:


        #editorial - divide into 2 groups
        T = sum(stones)
        n = len(stones)
        @cache
        def dp(i, ssum):
            if i == n:
                other = T - ssum
                return abs(other - ssum)
            
            a = dp(i+1, ssum + stones[i])
            b = dp(i+1, ssum)

            return min(a,b)

        return dp(0, 0)