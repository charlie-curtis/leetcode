class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:

        #you can either jump to the next idx that is >= nums[i]
        #or you can jump to the next IDX that is strictly less than you

        n = len(nums)
        nxt_lt = [-1]*n
        nxt_gte = [-1]*n

        stack1 = []
        stack2 = []
        for i in range(n-1, -1, -1):
            while stack1 and nums[stack1[-1]] >= nums[i]:
                stack1.pop()
            if stack1:
                nxt_lt[i] = stack1[-1]
            stack1.append(i)

            while stack2 and nums[stack2[-1]] < nums[i]:
                stack2.pop()
            if stack2:
                nxt_gte[i] = stack2[-1]
            stack2.append(i)



        @cache
        def dp(i):
            if i + 1 == n:
                return 0
            
            routes = [nxt_lt[i], nxt_gte[i]]
    
            ans = 1e15
            for x in routes:
                if x != -1:
                    ans = min(ans, dp(x) + costs[x])
            return ans
    
        return dp(0)
    