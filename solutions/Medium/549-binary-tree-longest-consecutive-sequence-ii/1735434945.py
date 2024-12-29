# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        d = defaultdict(set)
        def dfs(node):
            if not node:
                return
            
            if node.left:
                d[node].add(node.left)
                d[node.left].add(node)
            if node.right:
                d[node].add(node.right)
                d[node.right].add(node)

            dfs(node.left)
            dfs(node.right)


        dfs(root)


        seen = set()
        nodes = sorted(d.keys(), key=lambda x: x.val)

        def dfs2(node):
            if node in seen:
                return 0
            seen.add(node)
            
            best = 1
            for u in d[node]:
                if u.val == node.val+1:
                    best = max(best, 1 + dfs2(u))
            return best


        return max([dfs2(x) for x in nodes])
