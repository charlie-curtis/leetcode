class Solution:
    def rob(self, A: List[int]) -> int:

        if len(A) == 1:
            return A[0]

        def dp(A):
            n = len(A)
            cur = [A[0],0]
            prev = [A[0],0]
            for i in range(1,n):
                #rob
                cur[0] = prev[1] + A[i]
                #don't rob
                cur[1] = max(prev)
                prev = cur.copy()

            return max(cur)


        a = A[:-1]
        b = A[1:]
        return max(dp(a), dp(b))

        