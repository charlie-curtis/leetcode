class Solution:
    def minOperations(self, n: int) -> int:

        A = [2*i+1 for i in range(n)]
        print(A)

        med = median(A)
        print(med)
        ans = 0
        for i in range(n//2):
            ans+=med-A[i]
        return int(ans)
            
        