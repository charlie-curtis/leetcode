class Solution:
    def maxProfit(self, inventory: List[int], k: int) -> int:

        C = Counter(inventory)

        pq = []
        for v,f in C.items():
            heappush(pq, [-v, f])

        ans = 0
        MOD = 10**9+7

        def range_sum(x,y):
            a = x*(x+1)//2
            b = y*(y+1)//2
            return a-b
        ssum = 0
        while k > 0:
            #print("pq is", pq, "and k is", k)
            found = True
            while len(pq) > 1 and found:
                #consolidate
                found = False
                v,f = heappop(pq)
                v2,f2 = heappop(pq)
                #print("popped", v,v2, "with freqs", f, f2)
                if v == v2:
                    found = True 
                    heappush(pq, [v, f+f2])
                    #print("merging", v, "with freqs", f, f2)
                else:
                    #print("could not merge")
                    heappush(pq, [v, f])
                    heappush(pq, [v2, f2])
                
            v, f = heappop(pq)
            v = - v
            if len(pq) == 0:
                lower = 0
            else:
                lower = -pq[0][0]

            available = (v - lower)*f
            if k > available:
                #print("available was", available)
                k-=available
                ssum+=f*range_sum(v, lower)
                ssum%=MOD
                heappush(pq, [-lower, f])
            else:
                whole = k//f
                k-=f*whole
                ssum+=f*(range_sum(v, v-whole))
                ssum%=MOD
                new = v-whole
                ssum+=new*k
                ssum%=MOD
                break

        return ssum
        