class Solution:
    def maxPower(self, s: str) -> int:

        ans = 0
        for x, g in groupby(s):
            ans = max(ans, len(list(g)))
        return ans
        