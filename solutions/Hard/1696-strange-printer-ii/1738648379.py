class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:

        m,n = len(grid), len(grid[0])
        rowVals = {}
        colVals = {}

        seen = set()
        for i in range(m):
            for j in range(n):
                grid[i][j]-=1
                c = grid[i][j]
                seen.add(c)
                if c not in rowVals:
                    rowVals[c] = [i,i]
                else:
                    rowVals[c] = [min(rowVals[c][0], i), max(rowVals[c][1], i)]
                
                if c not in colVals:
                    colVals[c] = [j,j]
                else:
                    colVals[c] = [min(colVals[c][0], j), max(colVals[c][1], j)]


        d = defaultdict(set)
        indegree = Counter()
        for x in seen:
            x1,x2 = rowVals[x]
            y1,y2 = colVals[x]

            for i in range(x1, x2+1):
                for j in range(y1,y2+1):
                    v = grid[i][j]
                    if v != x and x not in d[v]:
                        d[v].add(x)
                        indegree[x]+=1
                    if v in d[x]:
                        return False


        adj = d
        V = {}
        WHITE = 0
        GREY = 1
        BLACK = 2
        def dfs(cur):
            if cur in V and V[cur] == GREY:
                return True

            if cur in V and V[cur] == BLACK:
                return False

            V[cur] = GREY
            for u in adj[cur]:
                if dfs(u):
                    return True
            V[cur] = BLACK
            return False

        for x in seen:
            if dfs(x):
                return False 
        return True
                
        q = deque()
        for u in adj.keys():
            if indegree[u] == 0:
                q.append(u)

        while q:
            idx = q.popleft()

            for u in adj[idx]:
                indegree[u]-=1
                if indegree[u] == 0:
                    q.append(u)

        return sum(indegree.values()) == 0