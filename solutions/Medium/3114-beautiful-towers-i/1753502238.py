class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:


        def compute(A):
            n = len(A)
            dp = [0]*n

            stack = []
            for i in range(n):
                while stack and A[stack[-1]] >= A[i]:
                    stack.pop()
                j = stack[-1] if stack else -1
                dp[i] = dp[j] + (i-j)*A[i]
                stack.append(i)
            return dp
        
        lefts = compute(heights)
        rights = compute(heights[::-1])[::-1]

        return max([l+r-v for l,r,v in zip(lefts,rights,heights)])