class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:

        n = len(A)
        j = 0
        ssum = 0
        ans = 0
        for i in range(n):
            ssum+=A[i]
            while (i-j+1)*ssum >=k:
                ssum-=A[j]
                j+=1
            ans+=(i-j+1)
        return ans
            


        