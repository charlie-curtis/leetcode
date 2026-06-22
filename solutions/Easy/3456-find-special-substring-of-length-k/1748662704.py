class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:


        for c, li in groupby(s):
            l = len(list(li))
            if l == k:
                return True
        return False