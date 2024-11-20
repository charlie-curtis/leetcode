class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:

        children = defaultdict(list)
        for i,x in enumerate(parent):
            children[x].append(i) 


        marked = set()
        def dfs(node):
            
            ssum = value[node] 
            for x in children[node]:
                ssum+=dfs(x)

            if ssum == 0:
                marked.add(node)

            return ssum

        def dfs2(node):
            if node in marked:
                return 0

            ans = 1
            for x in children[node]:
                ans+=dfs2(x)

            return ans
        


        dfs(0)
        return dfs2(0)
        print(marked)
            
        