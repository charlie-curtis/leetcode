class Solution:
    def maxScore(self, tmp: List[List[int]]) -> int:

        n = len(tmp)
        edges = defaultdict(list)

        for i in range(n):
            p,w = tmp[i]
            edges[p].append([i,w])

        @cache
        def dfs(node, usable):

            picksum = 0
            for u,w in edges[node]:
                #sum if we don't pick any of our outgoing edges and rely on our children
                picksum+=dfs(u, True)

            if not usable:
                return picksum

            ans = picksum 
            for u,w in edges[node]:
                ans = max(ans, max(0,w) + picksum + dfs(u, False) - dfs(u, True))

            return ans

                

        return dfs(0, True)
