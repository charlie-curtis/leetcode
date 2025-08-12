class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:


        stack = []
        n = len(part)
        for x in s:
            stack.append(x)
            while len(stack) >= n and ''.join(stack[-n:]) == part:
                stack = stack[0:-n]
        return ''.join(stack)

        