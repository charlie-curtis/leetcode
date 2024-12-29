class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:

        n = len(coins)
        INF = 10**9 
        dp = [INF]*n
        pointer = [-1]*n
        dp[-1] = coins[-1] 

        #dp[i] = how much it costs to visit index i
        for i in range(n-1, -1, -1):
            if coins[i] == -1:
                continue
            for j in range(1, maxJump+1):

                if i - j < 0:
                    break
                if coins[i-j] == -1:
                    continue
                
                if dp[i-j] >= dp[i] + coins[i-j]:
                    dp[i-j] = dp[i] + coins[i-j]
                    pointer[i-j] = i

        if n == 1:
            return [1]
        if pointer[0] == -1:
            return []

        p = 0
        out = []
        while  p != -1:
            out.append(p+1)
            p = pointer[p]
        return out
