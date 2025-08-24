class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        C = Counter(nums)

        @cache
        def dp(x):
            if x >= 10**4+1:
                return 0
            
            return max([
                dp(x+2) + C[x]*x,
                dp(x+1)
            ])
        

        return dp(0)
        