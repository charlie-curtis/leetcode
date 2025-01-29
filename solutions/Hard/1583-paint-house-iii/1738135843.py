class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        m = len(houses)
        n = len(cost)
        @cache
        def dp(i,k, prev):
            if i == m:
                if k == target:
                    return 0
                return 1e15

            if houses[i] != 0:
                tmp = k if (houses[i] == prev) else k+1
                return dp(i+1, tmp , houses[i])

            best = 1e15
            for j in range(len(cost[i])):
                t = k if (j+1 == prev) else k+1
                best = min(best, cost[i][j] + dp(i+1, t, j+1))
            return best


        res = dp(0,0, -10000)
        if res >= 1e15:
            return -1
        else:
            return res
                

            
                
        