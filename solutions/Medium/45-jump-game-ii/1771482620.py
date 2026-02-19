class Solution:
    def jump(self, nums: List[int]) -> int:


        n = len(nums)
        @cache
        def dp(i):
            if i == n-1:
                return 0

            ans = 10**9
            for j in range(i+1, min(n, i+nums[i]+1)):
                ans = min(ans, dp(j) + 1)
            return ans

        return dp(0)

        