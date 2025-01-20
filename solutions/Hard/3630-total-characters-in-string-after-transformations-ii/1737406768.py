class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:

        MOD = 10**9 + 7
        def mat_multiply(A,B):
            m1,n1 = len(A), len(A[0])
            m2,n2 = len(B), len(B[0])

            if n1 != m2:
                raise ValueError("Wrong dimensions for multiplication")

            out = [[0 for _ in range(n2)] for _ in range(m1)]
            for i in range(m1):
                for j in range(n2):
                    for k in range(n1):
                        #all pairs should be from the ith row, jth col
                        a = A[i][k]*B[k][j]
                        out[i][j]+=a
                        out[i][j] %=MOD
            return out


        def mat_exp(A, t):
            m,n = len(A), len(A[0])
            if t == 0:
                raise ValueError("Why is T = 0?")
            if t == 1:
                return A

            if t % 2 == 0:
                B = mat_exp(A, t//2)
                return mat_multiply(B,B)
            else:
                B = mat_exp(A, t//2)
                return mat_multiply(mat_multiply(B,B),A)


        B = [[0 for _ in range(26)] for _ in range(26)]
        for i in range(26):
            x = nums[i]
            for j in range(1,x+1):
                B[i][(i+j)%26] = 1

        C = mat_exp(B, t)
        D = [0]*26
        for x in s:
            D[ord(x) - ord('a')]+=1

        E = mat_multiply([D], C)

        ans = 0
        for x in E[0]:
            ans+=x
            ans%=MOD
        return ans