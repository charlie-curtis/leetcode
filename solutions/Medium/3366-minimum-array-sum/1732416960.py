class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:


        ans = 1e15
        n = len(nums)
        @cache
        def dp(i, r1, r2):
            if i == n:
                return 0

            a = b = c = d = e = 1e15
            #here our are options
            #do nothing
            #divide
            #subtract
            #divide then subtract
            #subtract then divide
            a = nums[i] + dp(i+1, r1, r2)
            if r1 > 0:
                b = ceil(nums[i]/2) + dp(i+1, r1-1, r2)
            if r2 > 0 and nums[i]>=k:
                c = nums[i]-k + dp(i+1, r1, r2-1)
            if r1 > 0 and r2 > 0:
                cur = ceil(nums[i]/2)
                if cur >= k:
                    d = cur-k + dp(i+1, r1-1, r2-1)
            if r1 > 0 and r2 > 0:
                if nums[i] >=k:
                    cur = nums[i]-k
                    e = ceil(cur/2) + dp(i+1, r1-1, r2-1)

            return min(a,b,c,d,e)
        return dp(0, op1, op2)
        