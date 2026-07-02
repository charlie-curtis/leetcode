class Solution:
    def twoEggDrop(self, n: int) -> int:


        @cache
        def dp(floors, eggs):
            if eggs == 1 or floors == 1:
                #have to go one by one
                return floors

            ans = floors
            for x in range(1, floors + 1):
                #breaks
                a = dp(x-1, eggs-1) + 1
                #doesn't break
                b = dp(floors-x, eggs) + 1

                ans = min(ans, max(a,b))
            return ans
        

        return dp(n, 2)


        