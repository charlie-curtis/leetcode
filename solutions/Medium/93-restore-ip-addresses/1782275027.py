class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:


        out = []
        n = len(s)
        def bt(i, cur):
            if i >= n:
                if len(cur) == 4:
                    out.append('.'.join(cur))
                return

            if len(cur) > 4:
                return

            
            for j in range(i, len(s)):
                if 0 <= int(s[i:j+1]) <= 255 and (s[i] != '0' or i==j):
                    cur.append(s[i:j+1])
                    bt(j+1, cur)
                    cur.pop()
                else:
                    return
        
        bt(0, [])
        return out




        