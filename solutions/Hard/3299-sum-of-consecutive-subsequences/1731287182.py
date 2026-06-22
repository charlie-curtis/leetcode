class Solution:
    def getSum(self, nums: List[int]) -> int:

        n = len(nums)
        MOD = 10**9 + 7
        def calc(A):

            #dp[i] = sum ending with i
            C = Counter()
            dp = Counter()
            for x in A:
                me = C[x-1] + 1
                me%=MOD
                #update the counts
                C[x]+=me
                C[x]%=MOD

                dp[x]+=dp[x-1]%MOD
                dp[x]+=me*x%MOD
            return sum(dp.values()) % MOD
        

        a = calc(nums)
        b = calc(nums[::-1])
        c = sum(nums)
        return (a + b - c) % MOD