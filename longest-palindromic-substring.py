#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        n = len(s)

        def check(i, j):
            nonlocal best
            while i >= 0 and j < n and s[i] == s[j]:
                if j-i+1 > len(best):
                    best = s[i:j+1]
                i-=1
                j+=1
        
        for i in range(n):
            check(i,i)
            check(i,i+1)

        return best
        
