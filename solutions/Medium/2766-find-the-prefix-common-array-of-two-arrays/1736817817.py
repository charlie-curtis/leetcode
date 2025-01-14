class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = Counter()
        out = []
        cur = 0
        for a,b in zip(A,B):
            C[a]+=1
            if C[a] == 2:
                cur+=1
            C[b]+=1
            if C[b] == 2:
                cur+=1
            out.append(cur)
        return out


        