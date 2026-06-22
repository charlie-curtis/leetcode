class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        A = [i for i in range(len(s)-len(a)+1) if s[i:i+len(a)] == a]
        B = [i for i in range(len(s)-len(b)+1) if s[i:i+len(b)] == b]

        out = []
        j = 0
        for i in A:
            while j < len(B) and i-B[j] > k:
                j+=1
            if j < len(B) and abs(i-B[j]) <=k:
                out.append(i)
        return out
