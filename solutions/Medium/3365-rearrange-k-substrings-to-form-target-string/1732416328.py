class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:


        C = Counter()
        C2 = Counter()

        cnt = 0
        n = len(s)
        amt = n//k
        for i in range(0,n,amt):
            C[s[i:i+amt]]+=1
            C2[t[i:i+amt]]+=1

        return C == C2