class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:


        C = Counter()
        mx = 0
        for p,f,t in trips:
            C[f]+=p
            C[t]-=p
            mx = max(t, mx)
        
        cur = 0
        for i in range(0,mx+1):
            cur+=C[i]
            if cur > capacity:
                return False
        return True
        