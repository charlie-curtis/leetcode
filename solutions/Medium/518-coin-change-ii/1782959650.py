class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        @cache
        def dp(i, rem):
            if rem == 0:
                return 1
            if rem < 0 or i == len(coins):
                return 0

            a = dp(i, rem-coins[i])
            b = dp(i+1, rem)
            return a+b
        return dp(0, amount)
        