class Solution:
    def makePalindrome(self, s: str) -> bool:

        n = len(s)
        miss = 0
        for i in range(n):
            if s[i] != s[n-1-i]:
                miss+=1

        return miss <= 4
        