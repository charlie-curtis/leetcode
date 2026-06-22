class Solution:
    def sumOddLengthSubarrays(self, A: List[int]) -> int:


        n = len(A)
        ans = 0
        for i in range(n):
            for j in range(i,n):
                if (i-j+1) % 2 == 1:
                    ans+=sum(A[i:j+1])
        return ans
                    
        