class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        graph = [set() for _ in range(n)]

        for u,v in edges:
            u-=1
            v-=1
            graph[u].add(v)

        def can_dag(graph):
            indegree = Counter()
            for i in range(n):
                for nxt in graph[i]:
                    indegree[nxt]+=1
            q = []
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)
            if len(q) != 1:
                return False
            while q:
                node = q.pop()
                #print(node, n)
                for nxt in graph[node]:
                    indegree[nxt]-=1
                    if indegree[nxt] == 0:
                        q.append(nxt)
            return max(indegree.values()) == 0

        for i in range(len(edges)-1, -1, -1):
            u,v = edges[i]
            u-=1
            v-=1
            graph[u].remove(v)
            if can_dag(graph):
                return [u+1,v+1]
            graph[u].add(v)