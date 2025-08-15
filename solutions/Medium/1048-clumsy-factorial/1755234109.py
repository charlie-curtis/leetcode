class Solution:
    def clumsy(self, n: int) -> int:

        stack = []
        ops = ['*', '/', '+', '-']
        for i in range(n, 0, -1):
            stack.append(i)
            stack.append(ops[(n-i)%4])
        stack.pop()
        for i in range(2):
            tmp = []
            j = 0
            while j < len(stack):
                if stack[j] != ops[i]:
                    tmp.append(stack[j])
                    j+=1
                else:
                    x = tmp.pop()
                    y = stack[j+1]
                    if i == 0:
                        tmp.append(x*y)
                    elif i == 1:
                        tmp.append(x//y)
                    j+=2
            stack = tmp
        
        out = stack[0] 
        n = len(stack)
        j = 1
        while j < n:
            if stack[j] == '+':
                out+=stack[j+1]
            else:
                out-=stack[j+1]
            j+=2
        return out