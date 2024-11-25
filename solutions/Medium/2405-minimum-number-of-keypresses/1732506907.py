class Solution:
    def minimumKeypresses(self, s: str) -> int:

        C = Counter(s)
        pq = [1]*9
        ans = 0
        for v in sorted(C.values(), reverse=True):
            cur = heapq.heappop(pq)
            ans+=v*cur
            heapq.heappush(pq, cur+1)
        return ans
        