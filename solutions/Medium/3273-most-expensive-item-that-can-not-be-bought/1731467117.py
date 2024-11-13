class Solution:
    def mostExpensiveItem(self, p1: int, p2: int) -> int:


        end = p1*p2+1

        @cache
        def dp(x):
            if x < min(p1,p2):
                return False
            
            if x in [p1,p2]:
                return True
            return dp(x-p1) or dp(x-p2)


        ans = 0
        for x in range(end):
            if not dp(x):
                ans = x
        return ans
        