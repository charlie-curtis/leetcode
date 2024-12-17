class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:


        C = Counter(s)
        pq = []
        for k,v in C.items():
            pq.append([-ord(k),k,v])
        heapq.heapify(pq)



        out = []
        streak = 0
        while len(pq) > 0:
            _, k,v = heapq.heappop(pq)
            if streak == repeatLimit and k == out[-1]:
                if pq:
                    _, k2,v2 = heapq.heappop(pq)
                    out.append(k2)
                    if v2 > 1:
                        heapq.heappush(pq, [-ord(k2), k2, v2-1])
                    heapq.heappush(pq, [-ord(k), k, v])
            else:
                out.append(k)
                if v > 1:
                    heapq.heappush(pq, [-ord(k), k, v-1])
            
            if len(out) == 1 or out[-1] != out[-2]:
                streak = 1
            else:
                streak+=1
        return ''.join(out)