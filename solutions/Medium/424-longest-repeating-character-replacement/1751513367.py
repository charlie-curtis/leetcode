class Solution:
    def characterReplacement(self, s: str, k: int) -> int:




        best = 0
        n = len(s)
        ok = k
        for t in range(26):
            c = chr(t + ord('A'))
            j = 0
            k = ok
            for i in range(n):
                if s[i] != c:
                    k-=1
                while k < 0:
                    if s[j] != c:
                        k+=1
                    j+=1
                best = max(best, i-j+1)
        return best



        