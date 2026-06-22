class Solution:
    def getHappyString(self, n: int, k: int) -> str:


        ans = ""
        seen = 0
        def bt(cur):
            nonlocal ans, seen
            if len(cur) == n:
                seen+=1
                if seen == k:
                    ans = ''.join(cur)
                return

            for x in ['a','b', 'c']:
                if not cur or cur[-1] != x:
                    cur.append(x)
                    bt(cur)
                    cur.pop()
        bt([])
        return ans
                