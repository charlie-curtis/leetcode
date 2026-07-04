class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []
        for x in tokens:
            if x not in '+-/*':
                stack.append(int(x))
            else:
                s = str(stack[-2]) + x + str(stack[-1])
                stack.pop()
                stack.pop()
                res = eval(s)
                stack.append(int(res))
        return stack[-1]
        
        