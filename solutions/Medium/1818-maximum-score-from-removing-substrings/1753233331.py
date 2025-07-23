class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        d = {'a': 'a', 'b': 'b'}
        if y > x:
            #just reverse the mappings and do the same problem
            d = {'a': 'b', 'b': 'a'}
            x,y = y,x
        s = ''.join([d[x] if x in 'ab' else 'c' for x in s])
        A = s.split('c')

        def do(s):
            stack = []
            ans = 0
            for c in s:
                if not stack:
                    stack.append(c)
                elif c == 'b' and stack[-1] == 'a':
                    stack.pop()
                    ans+=x
                else:
                    stack.append(c)
            
            s = ''.join(stack)
            stack = []
            for c in s:
                if not stack:
                    stack.append(c)
                elif stack[-1] == 'b' and c == 'a':
                    stack.pop()
                    ans+=y
                else:
                    stack.append(c)
            return ans


        ans = 0
        for s in A:
            if not s:
                continue
            ans+=do(s)
        
        return ans
        