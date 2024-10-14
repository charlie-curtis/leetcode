class Solution:
    def maxSubstringLength(self, s: str) -> int:

        n = len(s)
        pref = [[0 for _ in range(26)] for _ in range(n+1)]
        lMost, rMost = {}, {}

        for i in range(n):
            idx = ord(s[i]) - ord('a')
            pref[i+1][idx]+=1
            for j in range(26):
                pref[i+1][j]+=pref[i][j]
            
            if s[i] not in lMost:
                lMost[s[i]] = i
            rMost[s[i]] = i


        ans = -1
        for i in lMost.values():
            for j in rMost.values():
                if j < i or (j-i+1 == n):
                    continue
                
                good = True
                for k in range(26):
                    lCount = pref[i][k]
                    rCount = pref[j+1][k]
                    total = rCount - lCount
                    # [l,r] must contain zero occurrences or all occurrences
                    if total != 0 and total != pref[-1][k]:
                        good = False
                        break
                
                if good:
                    ans = max(ans, j-i+1)

        return ans


