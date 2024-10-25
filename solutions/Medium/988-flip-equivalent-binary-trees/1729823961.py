# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 or not root2:
            return root1 == root2

        if root1.val != root2.val:
            return False

        def isEqual(a,b):

            if not a or not b:
                return a == b

            return a.val == b.val

        def check(a, b):

            if not a or not b:
                return a == b

            if not isEqual(a.left, b.left):
                a.left,a.right = a.right, a.left
            
            if not isEqual(a.left, b.left) or not isEqual(a.right, b.right):
                return False

            return check(a.left, b.left) and check(a.right, b.right)

        return check(root1, root2)
        