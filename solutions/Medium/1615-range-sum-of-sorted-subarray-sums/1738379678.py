class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        A = nums
        out = []
        for i in range(n):
            for j in range(i,n):
                out.append(sum(A[i:j+1]))

        MOD = 10**9 + 7
        out.sort()
        ans = 0
        for i in range(left-1, right):
            ans+=out[i]
            ans%=MOD
        return ans
            
            
            
        