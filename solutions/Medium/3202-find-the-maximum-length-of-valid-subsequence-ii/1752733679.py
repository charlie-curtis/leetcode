class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[Counter() for x in nums]
        ans=0
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                a=nums[i]+nums[j]
                a%=k
                dp[i][a] = max(dp[i][a], dp[j][a]+1)
                ans=max(dp[i][a],ans)
        return ans+1
                
        