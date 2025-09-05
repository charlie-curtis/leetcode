class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        C = Counter()
        for start,end in clips:
            C[start] = max(C[start], end)
        
        q = []
        e = -1
        ans = 0
        for i in range(0, time+1):
            #print(e)
            #print(e)
            if C[i] > 0:
                heapq.heappush(q, -C[i])
                #print("adding", C[i])
            if e >= i:
                continue
            if e + .5 == time:
                return ans
            if q and -q[0] >= i:
                ans+=1
                e = -heapq.heappop(q)
                print("using", e)
                e-=.5
            else:
                return -1
        return ans
        
            