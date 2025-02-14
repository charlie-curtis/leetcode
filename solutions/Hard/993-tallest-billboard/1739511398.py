class Solution:
    def tallestBillboard(self, r: List[int]) -> int:
        n=len(r)
        T=sum(r)
        
        def check():
            @cache
            def dp(i,b):
                if i==n:
                    return 0 if b == 0 else -1e15
                y=r[i]
                
                
                a= dp(i+1, b-y) + y
                d=dp(i+1,b+y) + y
                c=dp(i+1,b)
                return max(a,d,c)
            return dp(0,0)
            
        return check()//2