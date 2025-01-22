class Solution:
    def breakPalindrome(self, s: str) -> str:

        n = len(s)
        i = 0
        j = n-1
        if n == 1:
            return ""

        while i < j:
            v = ord(s[i]) - ord('a')
            for k in range(26):
                if k >= v:
                    break
                v2 = chr(k + ord('a'))
                return s[:i] + v2 + s[i+1:]
            i+=1
            j-=1

        if s[-1] != 'a':
            return s[:-1] + "a"
        else:
            return s[:-1] + "b"