class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        j = n-1
        i = 0
        while i < j:
            if s[i] != s[j]:
                return 2
            i+=1
            j-=1
        return 1
        