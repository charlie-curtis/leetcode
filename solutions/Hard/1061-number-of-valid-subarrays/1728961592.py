class Solution:
    def validSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        nxt_smaller = [n]*n

        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                nxt_smaller[i] = stack[-1]
            stack.append(i)
        
        ans = 0
        for i in range(n):
            j = nxt_smaller[i]
            ans+=j-i
        return ans

        