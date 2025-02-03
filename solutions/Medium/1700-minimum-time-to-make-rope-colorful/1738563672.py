class Solution:
    def minCost(self, colors: str, T: List[int]) -> int:


        n = len(colors)
        memo = {}
        def dp(i,prev, memo):
            if i == n:
                return 0

            if (i,prev) in memo:
                return memo[(i,prev)]


            #remove my color
            a = T[i] + dp(i+1, prev, memo)
            b = 1e15
            if colors[i] != prev:
                #leave my color
                b = dp(i+1, colors[i], memo)


            memo[(i,prev)] = min(a,b)
            return min(a,b)
        return dp(0, -1, {})
            
        