class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        n = len(s)
        @cache
        def dp(i,j):

            if i >= j: return 0

            return dp(i+1,j-1) if s[i] == s[j] else 1 + min([dp(i+1, j), dp(i,j-1)])

        return dp(0,n-1) <= k
        