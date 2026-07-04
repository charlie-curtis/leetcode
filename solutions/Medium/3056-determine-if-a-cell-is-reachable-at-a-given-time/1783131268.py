class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        if (sx,sy) == (fx, fy):
            return t != 1

        d = max(abs(sx-fx), abs(sy-fy))
        return d <= t