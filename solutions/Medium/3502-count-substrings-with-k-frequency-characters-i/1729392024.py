class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        
        n = len(s)
        j = 0
        C = Counter()
        ans = 0
        for i in range(n):
            
            C[s[i]]+=1
            
            while max(C.values()) >=k:
                ans+=n-i
                C[s[j]]-=1
                j+=1
                
        return ans
                
            