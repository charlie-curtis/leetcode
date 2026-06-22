class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        A=[abs(ord(x)-ord(y)) for (x,y) in zip(s,t)]
        ans=0
        j=0
        n= len(s)
        ssum=0
        for i,x in enumerate(A):
            ssum+=x
            while ssum > maxCost:
                ssum-=A[j]
                j+=1
            ans=max(ans,i-j+1)
        
            
            
        return ans