# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def go(node):
            nonlocal ans
            if not node:
                return False
            a = go(node.left)
            if a:
                ans+=node.left.val
            go(node.right)
            return not node.left and not node.right
        go(root)
        return ans
        