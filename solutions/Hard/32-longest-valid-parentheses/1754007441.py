class Solution:
    def longestValidParentheses(self, s: str) -> int:

        #editorial - the general idea is dp[i] stores the longest VALID answer ending at s[i-1], and then we try to extend it by checking the character next to us (e.g. '()' or checking a double nested paren (e.g. '(())')
        n = len(s)
        dp = [0]*(n+1)

        ans = 0
        for i in range(1,n):
            if s[i] == ')':
                if s[i-1] == '(': #completed wtih char right next to us
                    dp[i+1] = dp[i-1] + 2
                if s[i-1] == ')':
                    #()(())
                    j = dp[i]
                    if i-j-1 >= 0 and s[i-j-1] == '(':
                        dp[i+1] = max(dp[i+1], dp[i-j-1] + dp[i] + 2)
            ans = max(ans, dp[i+1])
        #print(dp)
        return ans
            
