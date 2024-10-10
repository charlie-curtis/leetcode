# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:

        def getHeight(node):

            isLeaf = (node.left and node.left.right == node) or (node.right and node.right.left == node)

            if isLeaf:
                return 0

            a = b = 0
            if node.left:
                a = 1 + getHeight(node.left)
            if node.right:
                b = 1 + getHeight(node.right)
            
            return max(a,b)
            

        return getHeight(root)

        

        