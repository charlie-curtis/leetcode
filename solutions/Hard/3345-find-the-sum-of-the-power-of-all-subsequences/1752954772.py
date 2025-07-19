class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:

        MOD = 10**9 + 7
        n = len(nums)
        @cache
        def dp(i, v, s):
            if i == len(nums):
                if v != 0:
                    return 0
                return pow(2,n-s, MOD)
            if v < 0:
                return 0
            
            a = dp(i+1, v-nums[i], s+1)
            b = dp(i+1, v, s)

            return (a+b) % MOD
        
        ans = dp(0, k, 0)
        dp.cache_clear()
        return ans