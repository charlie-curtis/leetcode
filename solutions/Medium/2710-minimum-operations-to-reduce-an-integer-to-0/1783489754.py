class Solution:
    def minOperations(self, n: int) -> int:


        cut = log2(n)
        powers = [2**i for i in range(int(cut)+2)]

        cost = [10**9]*(2*n+1)

        q = deque([0])
        d = 0
        while cost[n] == 10**9:
            m = len(q)
            for _ in range(m):
                v = q.popleft()

                if cost[v] <= d:
                    continue
                cost[v] = d
                for p in powers:
                    if v + p < len(cost) and cost[v+p] > d+1:
                        q.append(v+p)
                    if v - p >= 0 and cost[v-p] > d+1:
                        q.append(v-p)
            d+=1
        return cost[n]