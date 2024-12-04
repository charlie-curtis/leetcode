class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        n = len(str2)

        def isgood(a,b):
            if a == b:
                return True
            i,j = ord(a) - ord('a'), ord(b) - ord('a')
            return (i+1)%26 == j

        i = 0
        for x in str1:
            if i == n:
                break
            if isgood(x, str2[i]):
                i+=1
        return i == n