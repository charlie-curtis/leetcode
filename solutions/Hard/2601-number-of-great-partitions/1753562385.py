class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:

        n = len(nums)
        MOD = 10**9 + 7
        T = sum(nums)
        wiggle = T - 2*k
        if wiggle < 0:
            return 0
        #editorial - solve the problem in reverse (# of partitions where subsets < k)
        @cache
        def dp(i, rem):
            if i == n:
                return int(rem > 0)
            if rem == 0:
                return 0
            
            a = dp(i+1, rem)
            b = dp(i+1, max(0,rem-nums[i]))

            return (a + b) % MOD
        
        return ((2**n % MOD) - 2*dp(0, k)) % MOD
            


        