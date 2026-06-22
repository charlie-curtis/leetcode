class Solution:
    def minSwaps(self, s: str) -> int:

        stack = []

        for x in s:
            if x == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(x)

        x = len(stack)
        y = 4
        return (x+y-1)//y
        