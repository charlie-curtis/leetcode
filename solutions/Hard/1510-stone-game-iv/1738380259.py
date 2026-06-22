class Solution:
    def winnerSquareGame(self, n: int) -> bool:


        @cache
        def dp(x):

            i = 1
            while i*i <= x:
                if not dp(x-i*i):
                    return True
                i+=1
            return False
        return dp(n)
        