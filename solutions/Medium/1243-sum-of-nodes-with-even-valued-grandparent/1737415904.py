# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(cur, p, gp):
            if not cur:
                return
            nonlocal ans

            if gp % 2 == 0:
                ans+=cur.val

            dfs(cur.left, cur.val, p)
            dfs(cur.right, cur.val, p)
        dfs(root, 1, 1)
        return ans

            
        