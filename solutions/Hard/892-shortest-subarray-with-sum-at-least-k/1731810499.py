class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:


        nums = [0,-1] + nums
        q = deque()

        n = len(nums)

        ans = 1e15 
        ssum = 0
        for i in range(n):
            ssum+=nums[i]

            while q and ssum - q[0][0] >= k:
                j = q.popleft()[1]
                ans = min(ans, i-j)

            
            while q and q[-1][0] >= ssum:
                q.pop()
            q.append([ssum,i])


        return ans if ans != 1e15 else -1
        