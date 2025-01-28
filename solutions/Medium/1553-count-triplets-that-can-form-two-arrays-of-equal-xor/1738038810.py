class Solution:
    def countTriplets(self, A: List[int]) -> int:

        n = len(A)

        #i will be the end of a, i+1 will be the start of b
        ans = 0
        for i in range(n-1):

            C = Counter()
            cur = 0
            for j in range(i, -1, -1):
                cur^=A[j]
                C[cur]+=1

            cur = 0
            for j in range(i+1,n):
                cur^=A[j]
                ans+=C[cur]
        return ans
                
                
                
                
        