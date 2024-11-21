class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:

        d = defaultdict(int)
        for x in queries:
            d[x]+=1

        ans = 0
        def dfs(node, cur):
            nonlocal ans
            if node > n:
                return

            cur+=d[node]
            ans+=cur%2

            dfs(2*node, cur)
            dfs(2*node+1, cur)


        

        dfs(1, 0)
        return ans
        