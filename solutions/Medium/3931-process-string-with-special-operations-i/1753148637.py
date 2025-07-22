class Solution:
    def processStr(self, s: str) -> str:


        stack = []
        for x in s:
            if x == '*':
                if stack:
                    stack.pop()
            elif x == '#':
                stack+=stack
            elif x == '%':
                stack = stack[::-1]
            else:
                stack.append(x)
        return ''.join(stack)
        