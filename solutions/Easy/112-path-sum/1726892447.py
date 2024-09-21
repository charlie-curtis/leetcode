# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def go(node, cur):
            if not node:
                return False
            if not node.left and not node.right:
                return node.val+cur == targetSum
            
            return go(node.left, cur + node.val) or go(node.right, cur + node.val)

        return go(root, 0)

        