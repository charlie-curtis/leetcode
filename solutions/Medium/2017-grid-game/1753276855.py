class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        A=grid[0]
        B=grid[1]

        
        
        n=len(A)
        def check(A,B):
            pre=list(accumulate(A,initial=0))
            pre1=list(accumulate(B,initial=0))

            ans=float('inf')
            for i in range(n):
                a = pre1[i]
                b=pre[-1]-pre[i+1]
                ans=min(ans,max(a,b))
            return ans
        return check(A,B)