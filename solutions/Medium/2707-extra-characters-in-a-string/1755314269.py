class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        d = set(dictionary)
        n = len(s)

        @cache
        def dp(i):
            if i == n:
                return 0
            
            ans = 10**9 
            for j in range(i,n):
                if s[i:j+1] in d:
                    ans = min(ans, dp(j+1))
            ans = min(ans, dp(i+1)+1)
            return ans
        return dp(0)

        