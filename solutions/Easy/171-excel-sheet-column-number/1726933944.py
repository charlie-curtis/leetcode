class Solution:
    def titleToNumber(self, title: str) -> int:

        ans = 0
        multi = 1
        for c in reversed(title):
            v = ord(c) - ord('A') + 1
            ans+= v*multi
            multi*=26

        return ans
        