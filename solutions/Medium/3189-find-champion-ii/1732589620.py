class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        in_degree = Counter()
        for i in range(n):
            in_degree[i]+=0

        for u,v in edges:
            in_degree[v]+=1

        cans = []
        for i in range(n):
            if in_degree[i] == 0:
                cans.append(i)

        return cans[0] if len(cans) == 1 else -1

        