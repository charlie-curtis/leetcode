# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def go(a, b):
            if not a or not b:
                return a == b
            if a.val != b.val:
                return False
            return go(a.right, b.left) and go(b.right, a.left)

        return go(root.left, root.right)
        