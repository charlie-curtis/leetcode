class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:


        n = len(days)
        @cache
        def dp(i):

            if i == n:
                return 0

            day = days[i]
            passes = [1,7,30]
            best = 1e15
            for i,x in enumerate(passes):
                j = bisect_left(days, day + x)
                best = min(best, dp(j)  + costs[i])
            return best
        
        return dp(0)
        