class Solution:
    def smallestValue(self, n: int) -> int:

        def get(n):
            out=[]
            x=2
            while x*x<=n:
                while n%x==0:
                    out.append(x)
                    n//=x
                x+=1 if x==2 else 2
            if n!=1: out.append(n)
            return out
        prev=-1
        while prev!=n:
            prev=n
            pfs=get(n)
            n=sum(pfs)
        return n