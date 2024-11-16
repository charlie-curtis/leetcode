class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:


        n = len(s)

        @cache
        def dp(i,j, avoid):
            if i >= j:
                return 0

            options = [0]
            if s[i] == s[j] and s[j] != avoid:
                options.append(1 + dp(i+1, j-1, s[i]))
            else:
                options.append(dp(i+1, j, avoid))
                options.append(dp(i, j-1, avoid))

            res = max(options)
            return res

            


        return dp(0, n-1, '')*2