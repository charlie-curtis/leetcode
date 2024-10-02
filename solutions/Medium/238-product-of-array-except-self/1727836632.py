class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        
        n = len(A)
        pre = [0]*n
        suf = [0]*n

        pre[0] = A[0]
        suf[-1] = A[-1]

        for i in range(1, n):
            pre[i]=pre[i-1]*A[i]
        for i in range(n-2, -1, -1):
            suf[i]=suf[i+1]*A[i]

        out = []
        for i in range(n):
            p = 1 if i == 0 else pre[i-1]
            s = 1 if i == n-1 else suf[i+1]
            out.append(p*s)
        return out


        