class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l = 0
        r = 2**31
        while l <= r:
            mid = l + (r-l)//2
            v = mid*mid
            if v == num:
                return True
            if v < num:
                l = mid + 1
            else:
                r = mid -1
        return False

        