class Solution:
    def reverseParentheses(self, s: str) -> str:


        stack = []
        for x in s:
            if x == ')':
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop()[0])
                stack.pop()
                stack+=tmp
            else:
                stack.append(x)
        return ''.join(stack)
