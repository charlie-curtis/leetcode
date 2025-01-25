class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)
        @cache
        def dp(i):
            if i == n:
                return 0

            ans = -1e15 
            ssum = 0
            for j in range(i,min(n, i+3)):
                ssum+=stoneValue[j]
                ans = max(ans, ssum-dp(j+1))

            return ans

        res = dp(0)
        #print("res", res)
        if res == 0:
            return "Tie"
        elif res > 0:
            return "Alice"
        else:
            return "Bob"

                
            
        