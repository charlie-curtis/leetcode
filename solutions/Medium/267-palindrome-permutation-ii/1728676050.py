class Solution:
    def generatePalindromes(self, s: str) -> List[str]:


        C = Counter(s)
        odds = [[k,v] for k,v in C.items() if v % 2 == 1]
        if len(odds) > 1:
            return []

        base = odds[0][0] if odds else ""
        if base:
            C[base]-=1

        ans = set()
        def bt(cur, tmp):

            if sum(tmp.values()) == 0:
                ans.add(cur)
            
            options = tmp.keys()
            for k in options:
                if tmp[k] > 0:
                    tmp[k]-=2
                    bt(k + cur + k, tmp)
                    tmp[k]+=2


        bt(base, C)
        return list(ans)


        