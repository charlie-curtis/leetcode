class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        n=len(nums)
        dp = [1]*n
        prev = [-1]*n
        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
                        prev[i] = j
                    ans = max(ans, dp[i])
        
        out = []
        for i in range(n):
            if ans == dp[i]:
                j = i
                while j != -1:
                    out.append(nums[j])
                    j = prev[j]
                return out
        raise ValueError("Wrong")