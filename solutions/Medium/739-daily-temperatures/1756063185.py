class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:

        n = len(A)

        out = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                stack.pop()
            if stack:
                out[i] = stack[-1] - i
            stack.append(i)
        return out
        