# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def count(node):
            nonlocal ans
            if not node:
                return True
            a = count(node.left)
            b = count(node.right)

            a_good = a and (not node.left or node.left.val == node.val)
            b_good = b and (not node.right or node.right.val == node.val)
            if a_good and b_good:
                ans+=1
            return a_good and b_good

        count(root)
        return ans
        