class Solution:
    def minLength(self, s: str) -> int:

        stack = []
        for x in s:
            if x == 'B' and stack and stack[-1] == 'A':
                stack.pop()
            elif x == 'D' and stack and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(x)
        return len(stack)
        