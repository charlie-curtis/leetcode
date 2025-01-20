class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        MOD=10**9+7
        C = Counter(s)

        @cache
        def dp(v, t):
            d = 26 - v
            if d > t:
                return 1
            return (dp(0, t-d) + dp(1, t-d)) % MOD


        ans = 0
        for x in s:
            ans+=dp(ord(x) - ord('a'), t)
            ans%=MOD
        return ans
        
        