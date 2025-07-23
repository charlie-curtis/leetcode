class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        out = []
        def bt(cur, b):
            if b < 0:
                return
            if len(cur) == 2*n:
                if b == 0:
                    out.append(''.join(cur))
                return

            
            cur.append(')')
            bt(cur, b-1)
            cur.pop()
            cur.append('(')
            bt(cur, b+1)
            cur.pop()
            
            
            

        bt([], 0)
        return out
