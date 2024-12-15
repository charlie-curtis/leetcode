class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:


        n = len(nums)
        to_left = [-1]*n
        to_right = [n]*n

        stack = []
        for i in range(n):

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                to_left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                to_right[i] = stack[-1]
            stack.append(i)

        
        out = []
        for i in range(n):
            l = to_left[i]+1
            r = to_right[i]-1
            out.append(r-l+1)

        return out


        