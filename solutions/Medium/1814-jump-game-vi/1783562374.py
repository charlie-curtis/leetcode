class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:


        n = len(nums)
        dp = [float('-inf')]*(n)


        q = deque()
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
                q.append(i)
                continue

            while q and i - q[0] > k:
                tmp = q.popleft()
            dp[i] = max(dp[i], dp[q[0]] + nums[i])
            while q and dp[q[-1]] <= dp[i]:
                tmp = q.pop()
            q.append(i)

        
        return dp[-1]
        