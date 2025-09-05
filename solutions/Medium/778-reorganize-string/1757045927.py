class Solution:
    def reorganizeString(self, s: str) -> str:

        C = Counter(s)
        q = [[-v,k] for k,v in C.items()]
        heapify(q)

        A = []

        while q:
            if not A or q[0][1] != A[-1]:
                cnt,k = heapq.heappop(q)
                A.append(k)
                cnt+=1
                if cnt < 0:
                    heapq.heappush(q, [cnt, k])
            else:
                cnt,k = heapq.heappop(q)
                if not q:
                    return ""
                cnt2,k2 = heapq.heappop(q)
                A.append(k2)
                cnt2+=1
                if cnt2 < 0:
                    heapq.heappush(q, [cnt2, k2])
                heapq.heappush(q, [cnt, k])
        return ''.join(A)

        