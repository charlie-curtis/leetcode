class Solution:
    def maximumBeauty(self, f: List[int]) -> int:

        n = len(f)

        pos_pref = [0]*n
        lefts = {}
        rights = {}

        for i in range(n):
            pos_pref[i] = max(0, f[i])

            if f[i] not in lefts:
                lefts[f[i]] = i
            rights[f[i]] = i

            if i > 0:
                pos_pref[i]+=pos_pref[i-1]


        best = -10e15
        for i,x in enumerate(f):
            l = lefts[x]
            r = rights[x]

            if l == r:
                continue
            best = max(best, 2*x + pos_pref[r-1] - pos_pref[l])
        return best

        
        