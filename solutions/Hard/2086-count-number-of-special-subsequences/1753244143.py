class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:

        MOD=10**9+7
        n=len(nums)
        @cache
        def dp(i, prev):
            if i == n:
                return int(prev==2)
            use = 0
            if nums[i]-1 == prev or nums[i] == prev:
                use = dp(i+1, nums[i])
            dont = dp(i+1, prev)
            return (use+dont)%MOD
        res= dp(0,-1)
        dp.cache_clear()
        return res

            
        