class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:


        MOD = 10**9 + 7
        n = len(nums)
        @cache
        def dp(i, v1, v2):
            if i == n:
                return int(v1 == v2 and v1 != -1)

            a = nums[i]

            ans= 0

            ans+= dp(i+1, a if v1 == -1 else gcd(v1, a), v2)
            ans%=MOD

            ans+= dp(i+1, v1, a if v2 == -1 else gcd(v2,a))
            ans%=MOD

            ans+=dp(i+1, v1,v2)
            ans%=MOD

            return ans


        return dp(0, -1, -1)