# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ans = True
        def go(node):
            nonlocal ans
            if not node:
                return 0
            ldepth = go(node.left)
            rdepth = go(node.right)
            if abs(ldepth - rdepth) > 1:
                ans = False
            return 1 + max(ldepth, rdepth)
        go(root)
        return ans
        