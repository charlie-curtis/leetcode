class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        C = Counter()
        for s,e,v in bookings:
            C[s]+=v
            C[e+1]-=v
        
        cur = 0
        out = []
        for i in range(1,n+1):
            cur+=C[i]
            out.append(cur)
        return out