class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
                

        #go til k, is it above n?


        if k > n:
            return 0
        if k == 0:
            return 1
        if k + maxPts <= n:
            return 1

        dp = [0]*(k+maxPts+1)
        last = deque([0]*maxPts)
        ssum = 0
        for i in range(n, -1, -1):
            if i >= k:
                dp[i] = 1
            else:
                dp[i] = ssum / maxPts
            
            last.append(dp[i])
            ssum+=dp[i]
            ssum-=last.popleft()
        return dp[0]