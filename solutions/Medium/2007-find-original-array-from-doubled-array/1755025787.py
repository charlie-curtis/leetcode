class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        n = len(changed)
        if n % 2 == 1:
            return [] 
        C = Counter(changed)

        out = []
        for k in sorted(C.keys()):
            while C[k] > 0:
                out.append(k)
                C[k]-=1
                if C[2*k] == 0:
                    return []
                C[2*k]-=1
        if len(out) != n//2 or sum(C.values()) != 0:
            return []
        return out

        