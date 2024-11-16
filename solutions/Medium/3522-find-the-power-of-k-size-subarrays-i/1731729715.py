class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:


        streak = 0 
        n = len(nums)
        q = deque()
        ans = [-1]*n
        #this was my original solution. it can be simplified because we know the maximum value in the window is going to be
        #the last element in your sliding window because a requirement of the sliding window is that it must be sorted ascending.
        for i in range(n-1, -1, -1):
            while q and q[0] - i >= k:
                q.popleft()

            if i == n-1 or nums[i+1] - nums[i] == 1:
                streak+=1
            else:
                streak = 1

            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

            if streak >= k:
                ans[i] = nums[q[0]]

        return ans[:n-k+1]