class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        #4123
        n = len(nums)
        ans = [-1]*n
        stack = []
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                j = stack.pop()
                if ans[j] == -1:
                    ans[j] = nums[i%n]
            stack.append(i%n)
        return ans

        #172654

        