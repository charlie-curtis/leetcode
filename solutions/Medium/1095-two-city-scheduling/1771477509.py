class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:


        #n=100, i = 50, so 5 * 10^3 input
        n = len(costs)
        @cache
        def dp(i,x):
            y = i-x
            if i == n:
                return 0
            
            a = b = 10**9
            if x < n//2:
                a = dp(i+1, x+1) + costs[i][0]
            if y < n//2:
                b = dp(i+1, x) + costs[i][1]

            return min(a,b)
        
        return dp(0,0)

        