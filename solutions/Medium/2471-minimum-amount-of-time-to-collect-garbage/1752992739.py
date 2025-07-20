class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n=len(garbage)

        ans=0
        st=set()
        for i in range(n-1,-1,-1):
            s=garbage[i]
            ans+=len(s)
            if i > 0:
                l= set([x for x in s])
                st=st.union(l)
                ans+=len(st)*travel[i-1]
        return ans