class Solution:
    def findValidPair(self, s: str) -> str:

        A = [int(x) for x in s]
        C = Counter(A)

        B = zip(A, A[1:])

        for i,(a,b) in enumerate(B):
            if a != b and C[a] == a and C[b] == b:
                return str(a) + str(b)
        return ""
        