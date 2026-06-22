class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:


        dp = [0]*n
        for i in range(1,n):
            if nums[i] - nums[i-1] <= maxDiff:
                dp[i] = dp[i-1] + 1

        out = []
        for i,j in queries:
            i,j = sorted([i,j])
            out.append(dp[j] - dp[i] == j-i)
        return out