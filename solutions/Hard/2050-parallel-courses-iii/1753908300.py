class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], cost: List[int]) -> int:

        indegree = Counter()
        adj = defaultdict(list)
        for u,v in relations:
            u-=1
            v-=1
            indegree[v]+=1
            adj[u].append(v)
        
        q = []
        times = [0]*n
        for i in range(n):
            if indegree[i] == 0:
                times[i] = cost[i]
                q.append(i)
            
        while q:
            node = q.pop()
            for nxt in adj[node]:
                times[nxt] = max(times[nxt], times[node] + cost[nxt])
                indegree[nxt]-=1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return max(times)

