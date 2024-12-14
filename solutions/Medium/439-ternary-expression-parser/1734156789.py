class Solution:
    def parseTernary(self, s: str) -> str:

        #my first solution took forever. the editorial had a cleaner solution

        stack = []
        n = len(s)
        i = n-1
        while i >= 0:
            if s[i] == ':':
                i-=1
            elif s[i] == '?':
                if s[i-1] == 'T':
                    #print(stack)
                    t = stack.pop(-2)
                    #print("removing", t)
                else:
                    t = stack.pop()
                    #print("removing X", t)
                i-=2
            else:
                stack.append(s[i])
                i-=1
        #print(stack)
        return stack[0]
