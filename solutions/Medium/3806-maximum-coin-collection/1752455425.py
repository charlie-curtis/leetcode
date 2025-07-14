class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:


        n = len(lane1)
        @cache
        def dp(i, lane, k):
            if i == n:
                return 0
            
            a = dp(i+1, lane, k) + (lane1[i] if lane == 1 else lane2[i])
            b = a
            c = 0
            if k > 0:
                b = dp(i+1, 1-lane, k-1) + (lane2[i] if lane == 1 else lane1[i])
            
            return max(a,b, c)

        a = max(max(lane1), max(lane2))
        if a < 0:
            return a
        return max([dp(i,1,2) for i in range(n)])

            