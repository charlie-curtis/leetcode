class Solution:
    def widestPairOfIndices(self, A: List[int], B: List[int]) -> int:

        n = len(A)

        balance = ans = 0
        d = {}
        d[0] = -1
        for i in range(n):
            if A[i]:
                balance+=1
            if B[i]:
                balance-=1
            
            if balance in d:
                ans = max(ans, i-d[balance])
            if balance not in d:
                d[balance] = i
        return ans


        