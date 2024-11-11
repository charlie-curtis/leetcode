class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        
        n = len(nums)
        MOD = 10**9 + 7

        C = Counter()
        dp = Counter()

        #dp[i] = sum of the subsequences ending at i 

        for x in nums:
            me = (C[x-1] + C[x+1] + 1) % MOD
            C[x]+=me
            C[x]%=MOD

            dp[x]+= (dp[x-1] + dp[x+1]) % MOD
            dp[x]%=MOD
            dp[x]+= me*x%MOD
            dp[x]%=MOD

        return sum(dp.values()) % MOD


        #1,2,3,3

        #C[1] = 1
        #C[2] = 2 [(1,2), 2]
        #C[3] = 3 ([1,2,3], [2,3], [3])
        #C[3]+= C[3] + 3 = 6 ([1,2,3], [2,3], [3]) (x2)