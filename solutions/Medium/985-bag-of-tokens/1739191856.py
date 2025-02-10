class Solution:
    def bagOfTokensScore(self, t: List[int], p: int) -> int:
        
        n=len(t)
        i,j=0,n-1
        ans=0
        s=0
        t.sort()
        
        while i <=j:
            if t[i] <= p:
                s+=1
                p-=t[i]
                i+=1
            elif s > 0:
                p+=t[j]
                s-=1
                j-=1
            else: break
            ans=max(ans, s)
        return ans
            
                
                
        
        