# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        ans = 1e10
        def go(node, depth):
            nonlocal ans
            if not node:
                return
            go(node.left, depth+1)
            go(node.right, depth+1)
            if not node.left and not node.right:
                ans = min(ans, depth)
        go(root, 1)
        return ans
        