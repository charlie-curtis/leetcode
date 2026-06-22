class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:

        n = len(nums)

        stack = []
        ans = 0
        for x in nums:
            best = 0 
            if stack and stack[-1] > x:
                continue
            stack.append(x)
        return len(stack)

        #4,1,2,5,6

        