class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        pref = [[0 for _ in range(26)] for _ in range(n+1)]

        for i in range(n):
            letter = s[i]
            k = ord(letter) - ord('a')

            for j in range(26):
                pref[i+1][j] = pref[i][j]
            
            pref[i+1][k]+=1

        out = []
        for l,r in queries:
            tmp = 0
            for i in range(26):
                cnt = pref[r+1][i] - pref[l][i]
                tmp+=(cnt*(cnt+1))//2
            out.append(tmp)
        return out

        