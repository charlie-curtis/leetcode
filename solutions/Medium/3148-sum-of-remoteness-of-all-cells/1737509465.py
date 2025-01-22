class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:


        n = len(grid)
        dsu = DisjointSetUnion(n*n)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    continue
                if i > 0 and grid[i-1][j] > -1:

                    me = i*n + j
                    you = (i-1)*n + j
                    dsu.union(me,you)

                if j > 0 and grid[i][j-1] > -1:

                    me = i*n + j
                    you = (i)*n + j-1
                    dsu.union(me,you)

        
        root_sums = defaultdict(int)
        for i in range(n):
            for j in range(n):

                if grid[i][j] == -1:
                    continue
                me = i*n + j
                root = dsu.find(me)
                root_sums[root]+= grid[i][j]

        total = sum(root_sums.values())

        ans = 0
        for i in range(n):
            for j in range(n):

                if grid[i][j] == -1:
                    continue
                me = i*n + j
                root = dsu.find(me)
                r = root_sums[root]
                ans+= total-r
        return ans

        