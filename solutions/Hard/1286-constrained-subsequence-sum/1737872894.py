class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        stack = deque()
        ans = -1e15 
        for i,x in enumerate(nums):
            while stack and i - stack[-1][0]  > k:
                #no longer good
                stack.pop()
            v = stack[-1][1] if stack else -1e15
            me = max(x, v+x)
            ans = max(ans, me)
            while stack and me > stack[0][1]:
                stack.popleft()
            stack.appendleft([i, me])
        return ans
        