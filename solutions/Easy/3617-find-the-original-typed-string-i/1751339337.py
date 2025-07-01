class Solution:
    def possibleStringCount(self, word: str) -> int:


        ans = 0
        for _, li in groupby(word):
            l = len(list(li))
            ans+= l-1
        return ans+1

        