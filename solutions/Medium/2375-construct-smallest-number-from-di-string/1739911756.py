class Solution:
    def smallestNumber(self, p: str) -> str:

        stack = [1]
        mmax = 1
        for c, t in groupby(p):
            l = len(list(t))
            
            li = []
            for i in range(l):
                li.append(mmax+i+1)
            mmax = li[-1]
            
            if c == 'I':
                for x in li: stack.append(x)
            else:
                t = stack.pop()
                for x in reversed(li): stack.append(x)
                stack.append(t)
        return ''.join([str(x) for x in stack])
