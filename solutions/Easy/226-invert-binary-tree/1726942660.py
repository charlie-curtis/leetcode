# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def go(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            go(node.left)
            go(node.right)
        go(root)
        return root
            
        