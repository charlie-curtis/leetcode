class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:


        #Find the nodes in the cycle (dfs?)
        #say there are 4 nodes in a cycle, connect all of them to node A (which is part of the cycle)
        #do BFS from node A to everywhere else

        d = defaultdict(set)
        for u,v in edges:
            d[u].add(v)
            d[v].add(u)


        cycleNodes = set()
        def dfs(node, p, backedge):


            if node in backedge:
                cycleNodes.add(node)
                return node

            backedge.add(node)
            for u in d[node]:
                if u == p:
                    continue
                cycle_start = dfs(u, node, backedge)
                if cycle_start != -1:
                    cycleNodes.add(node)
                    return cycle_start if cycle_start != node else -1
            backedge.remove(node)
            return -1

        
        dfs(0, -1, set())
        nodes = list(cycleNodes)
        first = nodes[0]
        for u,v in edges:
            if u in cycleNodes or v in cycleNodes:
                #make a direct connection to first node in cycle
                d[first].add(v)
                d[first].add(u)


        def bfs(node):

            ans = [0]*n
            q = deque()
            q.append(first)
            seen = set()
            seen.add(first)
            dst = 0
            while q:
                for i in range(len(q)):
                    idx = q.popleft()
                    ans[idx] = dst if idx not in cycleNodes else 0
                    for nxt in d[idx]:
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)
                dst+=1
            return ans

        return bfs(first)



        




        