class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        n = len(events)
        events.sort()
        tmp = [events[i][0] for i in range(n)]
        nxt = [bisect_left(tmp,e+1) for _,e,_ in events]

        @cache
        def dp(i,j):
            if j > k:
                return -1e20
            if i == n:
                return 0
            
            #either don't pick anything, or pick this event and go to the next eligible
            return max(dp(i+1, j), events[i][2] + dp(nxt[i], j+1))
        
        return dp(0,0)
        