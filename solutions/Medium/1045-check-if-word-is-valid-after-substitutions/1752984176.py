class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        for x in s:
            stack.append(x)
            while len(stack) >=3 and ''.join(stack[-3:]) == 'abc':
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack