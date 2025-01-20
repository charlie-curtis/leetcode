class Solution:
    def combinationSum4(self, A: List[int], target: int) -> int:


        n = len(A)
        @cache
        def dp(rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            
            ans = 0
            for x in A:
                ans+=dp(rem-x)
            return ans
        return dp(target)



        