class Solution:
    def minimumTime(self, s: str) -> int:


        locs = [i for i in range(len(s)) if s[i] == '1']
        if not locs:
            return 0
        n = len(locs)

        pre = [float('inf')]*(n+1)
        post = [float('inf')]*(n+1)
        post[n] = 0
        pre[0] = 0

        for i in range(n):
            x = locs[i]
            #remove everything til here
            a = x+1
            #use operation 3
            b = 2 + pre[i]
            pre[i+1] = min(a,b)
        
        for i in range(n-1,-1,-1):
            x = locs[i]
            a = len(s) - x

            b = 2 + post[i+1]
            post[i] = min(a,b)
        
        return reduce(min, [pre[i] + post[i] for i in range(n+1)])