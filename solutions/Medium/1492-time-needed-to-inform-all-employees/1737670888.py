class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adj = defaultdict(list)

        for i,x in enumerate(manager):
            adj[x].append(i)


        def dfs(cur):

            cost = informTime[cur] 
            other = 0
            for nxt in adj[cur]:
                other = max(other, dfs(nxt))

            return cost + other

        return dfs(headID)
        