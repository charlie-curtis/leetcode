# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def validate(A, B):
            if not A or not B:
                return A == B
            if A.val != B.val:
                return False
            return validate(A.left, B.left) and validate(A.right, B.right)

        return validate(p,q)
        