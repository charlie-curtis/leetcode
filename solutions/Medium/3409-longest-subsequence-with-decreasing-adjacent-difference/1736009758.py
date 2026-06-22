class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[0 for _ in range(301)] for _ in range(301)]

        a = nums[0]
        for i in range(0,301):
            dp[a][i] = 1


        #dp[i][j] = longest pref where I is the val and J is the abs diff

        ans = 1
        for i in range(1,n):
            for j in range(300, -1, -1):
                v = nums[i]
                
                a = b = c = 1
                if v-j >= 0:
                    a = dp[v-j][j] + 1
                if v+j<= 300:
                    b = dp[v+j][j] + 1
                if j == 300:
                    c = dp[v][j]
                else:
                    c = dp[v][j+1]

                dp[v][j] = max(a,b,c,1)

                ans = max(ans, dp[v][j])
        return ans