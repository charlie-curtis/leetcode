class Solution:
    def maxSumOfSquares(self, digits: int, target: int) -> str:

        C = Counter()
        while digits:
            for x in range(9,-1,-1):
                if target- x >= 0:
                    target-=x
                    C[x]+=1
                    digits-=1
                    break
        if digits or target:
            return ""
        out = ""
        for k in sorted(C.keys(), reverse=True):
            out+=str(k)*C[k]
        return out