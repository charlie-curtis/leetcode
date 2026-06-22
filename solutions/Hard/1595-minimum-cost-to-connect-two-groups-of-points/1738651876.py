class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:


        m,n = len(cost), len(cost[0])
        TERM2 = 2**n -1


        mins = [1e15]*n
        for i in range(m):
            for j in range(n):
                mins[j] = min(mins[j], cost[i][j])

        @cache
        def dp(i,s2):
            if i == m:
                #connect whatever is disconnected
                ans = 0
                for j in range(n):
                    if s2&(1<<j) == 0:
                        ans+=mins[j]

                return ans 
            

            best = 1e15 
            for j in range(n):
                can = cost[i][j] + dp(i+1, s2|(1<<j))
                best = min(best, can)
            return best


        return dp(0,0)
                    


            
        