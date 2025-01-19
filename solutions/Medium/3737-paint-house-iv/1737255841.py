class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:


        @cache
        def dp(i,j, prev1, prev2):
            if i > j:
                return 0


            best = 1e15
            for k in range(3):
                for l in range(3):
                    if k == l or k == prev1 or l == prev2:
                        continue
                    best = min(best, dp(i+1, j-1, k,l) + cost[i][k] + cost[j][l])
            return best




        return dp(0, n-1, -1, -1)
                    

            
            
        