class Solution:
    def countTexts(self, s: str) -> int:


        n = len(s)
        MOD = 10**9 + 7
        @cache
        def dp(i):
            if i == n:
                return 1
            
            j = i
            ans = 0
            while j < n and s[j] == s[i]:
                if (s[i] in '97' and j-i > 3) or (s[i] not in '97' and j-i > 2):
                    break
                ans+=dp(j+1)
                ans%=MOD
                j+=1
            return ans

        return dp(0)
        