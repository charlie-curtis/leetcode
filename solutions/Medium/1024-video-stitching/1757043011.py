class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        C = Counter()
        for start,end in clips:
            C[start] = max(C[start], end)
        
        q = []
        e = -1
        ans = 0
        for i in range(0, time+1):
            if C[i] > 0:
                heapq.heappush(q, -C[i])
            if e >= i:
                continue
            if q and -q[0] >= i:
                ans+=1
                e = -heapq.heappop(q)
                if e == time:
                    return ans
                e-=.5
            else:
                return -1
        return ans
        
            