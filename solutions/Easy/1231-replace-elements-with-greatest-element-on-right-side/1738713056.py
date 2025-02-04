class Solution:
    def replaceElements(self, A: List[int]) -> List[int]:

        n = len(A)
        j = -1
        out = [0]*n
        for i in range(n-1, -1, -1):
            if i == n-1:
                out[i] = -1
            else:
                out[i] = A[j]
            if j == -1 or A[i] > A[j]:
                j = i
        return out

        