# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d=defaultdict(list)
        def dfs(node, lvl):
            if not node:
                return
            d[lvl].append(node.val)
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)
        dfs(root,0)

        out= []

        for i in range(max(d.keys()), -1,-1):
            out.append(d[i])
        return out
        