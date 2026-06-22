class Solution:
    def minOperations(self, n: int, m: int) -> int:

        def sieve(n):

            p = [True]*(n+1)
            p[1] = p[0] = False
            x = 2
            while x*x <= n:
                i = 2
                if p[x]:
                    while x*i <= n:
                        p[x*i] = False
                        i+=1
                x+=1

            return p

        p = sieve(9999)

        ans = 1e15
        cur = [int(x) for x in str(n)]
        seen = {}
        seen[n] = n
        pq = [[n, cur, []]]
        def to_int(cur):
            return int(''.join([str(x) for x in cur]))

        it = 0
        ans = []
        while pq:
            cost, cur, trans = heapq.heappop(pq)
            v = to_int(cur)
            if p[v]:
                continue
            if v == m:
                return cost

            #print("trans", trans)
            #t = trans.copy()
            #t.append(cur.copy())
            t = []
            for i in range(len(cur)):
                if cur[i] != 0:
                    cur[i]-=1
                    v = to_int(cur)
                    if v not in seen or seen[v] > cost + v:
                        if cur[0] != 0:
                            seen[v] = cost + v
                            heapq.heappush(pq, [cost+v, cur.copy(), t])
                    cur[i]+=1
                if cur[i] != 9:
                    cur[i]+=1
                    v = to_int(cur)
                    if v not in seen or seen[v] > cost + v:
                        if cur[0] != 0:
                            seen[v] = cost + v
                            heapq.heappush(pq, [cost+v, cur.copy(), t])
                    cur[i]-=1
        return -1