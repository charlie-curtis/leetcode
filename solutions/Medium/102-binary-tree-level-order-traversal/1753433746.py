# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(list)
        if not root: return []


        def dfs(x,dep):
            if not x:
                return
            d[dep].append(x.val)
            dfs(x.left,dep+1)
            dfs(x.right,dep+1)

        dfs(root,0)

        mx=max(d.keys())
        return [d[i] for i in range(0,mx+1)]
        