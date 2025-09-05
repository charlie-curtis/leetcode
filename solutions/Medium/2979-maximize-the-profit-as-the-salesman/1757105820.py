class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        dp = [0]*(n)

        d = defaultdict(list)
        for start,end,gold in offers:
            d[end].append([start,gold])


        for i in range(n):
            if i > 0:
                dp[i] = dp[i-1]
            for start,gold in d[i]:
                a = dp[start-1] if start -1 >= 0 else 0
                dp[i] = max(dp[i], a + gold)
        
        return dp[-1]
            
