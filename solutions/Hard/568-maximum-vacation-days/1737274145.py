class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:


        adj = defaultdict(set)
        n = len(flights)
        k = len(days[0])
        for i in range(n):
            for j in range(n):
                if flights[i][j] == 1:
                    adj[i].add(j)
        #max score you could get if you're in city I on week J
        @cache
        def dp(i, j):
            if j == k:
                return 0
            #our score for being in the city this week
            ans = days[i][j]

            #if we stay in this city for the following week
            can = dp(i,j+1)
            for nxt in adj[i]:
                can = max(can, dp(nxt, j+1))
            
            return ans + can
        

        ans = 0
        for i in range(n):
            if i == 0 or flights[0][i] == 1:
                ans = max(ans, dp(i,0))
        return ans
            

            
