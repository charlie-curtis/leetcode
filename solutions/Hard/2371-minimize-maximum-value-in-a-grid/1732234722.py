class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:

        m,n = len(grid), len(grid[0])
        nums = grid

        d = defaultdict(list)
        in_degree = Counter()

        for i in range(m):
            li = []
            for j in range(n):
                li.append([nums[i][j], i, j])

            li.sort()
            _, k,l = li[0]
            in_degree[(k,l)]+=0
            for i in range(1,len(li)):
                _, prev_a,prev_b = li[i-1]
                _, a,b = li[i]
                in_degree[(a,b)]+=1
                d[(prev_a, prev_b)].append((a,b))

        for j in range(n):
            li = []
            for i in range(m):
                li.append([nums[i][j], i, j])

            li.sort()
            _, k,l = li[0]
            in_degree[(k,l)]+=0
            for i in range(1,len(li)):
                _, prev_a,prev_b = li[i-1]
                _, a,b = li[i]
                in_degree[(a,b)]+=1
                d[(prev_a, prev_b)].append((a,b))


        q = set()
        for i in range(m):
            for j in range(n):
                if in_degree[(i,j)] == 0:
                    q.add((i,j))

        rank = 1
        ans = [[0 for _ in range(n)] for _ in range(m)]
        while len(q) > 0:
            k = len(q)

            nxt = set()
            for i,j in q:
                ans[i][j] = rank
                for nxt_a, nxt_b in d[(i,j)]:
                    tup = (nxt_a,nxt_b)
                    in_degree[tup]-=1
                    if in_degree[tup] == 0:
                        nxt.add((nxt_a, nxt_b))
            q = nxt
            rank+=1
        return ans
