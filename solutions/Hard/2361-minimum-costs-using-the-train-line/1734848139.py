class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:


        n = len(regular)+1
        INF = 10**12
        d_express = [INF]*n
        d_regular = [INF]*n


        pq = [(0, 0, False)]


        while pq:

            cost, node, isExpress = heapq.heappop(pq)

            if isExpress and d_express[node] < cost:
                continue
            if not isExpress and d_regular[node] < cost:
                continue

            
            if isExpress:
                d_express[node] = cost
            else:
                d_regular[node] = cost

            if node == n-1:
                continue
            
            a = b = 1e15
            if isExpress:
                #cost to stay on the express line
                a = express[node]
                #cost to switch backto the regular line
                b = regular[node]
            else:
                #cost to switch to the express line
                a = express[node] + expressCost
                #cost to continue on the regular line
                b = regular[node]

            
            if cost + a < d_express[node+1]:
                heapq.heappush(pq, [cost+a, node+1, True])
                d_express[node+1] = cost + a
            if cost + b < d_regular[node+1]:
                heapq.heappush(pq, [cost+b, node+1, False])
                d_regular[node+1] = cost + b


        return [min(d_regular[i], d_express[i]) for i in range(1,n)]
