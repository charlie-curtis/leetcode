class Solution:
    def permute(self, n: int) -> List[List[int]]:

        out = []
        def bt(cur):
            if len(cur) == n:
                out.append(cur.copy())
                return

            for x in range(1,n+1):
                if (x not in cur) and (not cur or (cur[-1] % 2 != x %2)):
                    cur.append(x)
                    bt(cur)
                    cur.pop()


        
        bt([])
        return out
        