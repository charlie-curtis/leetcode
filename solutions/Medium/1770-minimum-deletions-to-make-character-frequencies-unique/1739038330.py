class Solution:
    def minDeletions(self, s: str) -> int:

        C = Counter(s)

        seen = set()
        ans = 0
        for v in sorted(C.values()):
            while v in seen and v > 0:
                ans+=1
                v-=1
            seen.add(v)
        return ans
            
        
        