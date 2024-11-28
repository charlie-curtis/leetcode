class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:

        edges = defaultdict(list)
        for u,v in corridors:
            edges[u].append(v)
            edges[v].append(u)


        #I was close to solving this on my own. My approach was to iterate over all the nodes, and for each node. Find the nodes that had a distance of 2, and find the nodes that had a distance of 1. If any of those nodes overlapped, there was a cyle of length 3
        def bfs(i, length):

            q = deque()
            q.append([i])

            out = []
            while q:
                path = q.popleft()
                if len(path) == length:
                    out.append(path[-1])
                    continue

                last = path[-1]
                for u in edges[last]:
                    if u not in path and u > last:
                        q.append([x for x in path + [u]])

            return out


        
        ans = 0
        for i in edges.keys():
            C = Counter(bfs(i,3))
            for x in bfs(i,2):
                ans+=C[x]
        return ans