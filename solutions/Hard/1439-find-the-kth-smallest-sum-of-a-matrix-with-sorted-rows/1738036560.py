class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        pq = []
        m, n = len(mat), len(mat[0])

        ssum = 0
        for i in range(m):
            ssum+=mat[i][0]

        pq.append((ssum, tuple([0]*m)))

        seen = set()
        while pq:
            k-=1
            cur, state = heappop(pq)
            if k == 0:
                return cur

            for j in range(m):
                if state[j]+1 < n:
                    idx = state[j]
                    tmp = list(state)
                    tmp[j]+=1
                    nxt = (cur - mat[j][idx] + mat[j][idx+1], tuple(tmp))
                    if nxt not in seen:
                        heappush(pq, nxt)
                        seen.add(nxt)