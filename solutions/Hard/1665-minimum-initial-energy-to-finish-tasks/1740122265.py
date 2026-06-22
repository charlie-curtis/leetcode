class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        pq = []
        for a,m in tasks:
            heappush(pq, [a-m, -m, -a, a,m])

        cur = needed = 0
        while len(pq) > 0:
            _, _, _, a,m = heappop(pq)
            #print("processing", a,m)
            if m > cur:
                needed+=m-cur
                cur = m
            cur-=a
        return needed