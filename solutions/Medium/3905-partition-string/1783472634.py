class Solution:
    def partitionString(self, s: str) -> List[str]:


        seen=set()
        out=[]
        cur=""
        for x in s:
            cur+=x
            if cur not in seen:
                seen.add(cur)
                out.append(cur)
                cur=""

        return out
        