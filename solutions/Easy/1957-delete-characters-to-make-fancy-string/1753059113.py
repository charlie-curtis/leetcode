class Solution:
    def makeFancyString(self, s: str) -> str:

        stack = []

        for x in s:
            if len(stack) < 2 or (stack[-1] != x or stack[-2] != x):
                stack.append(x)

        return ''.join(stack)
        