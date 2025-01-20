class Solution:
    def xorQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:

        pref = [0]
        cur = 0
        for x in A:
            cur^=x
            pref.append(cur)

        out = []
        for l,r in queries:
            out.append(pref[r+1] ^pref[l])
        return out
            
        