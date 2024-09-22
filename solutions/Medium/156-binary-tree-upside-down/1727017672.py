# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        newRoot = None
        def dfs(node, isLeft, parent, parent_right):
            nonlocal newRoot
            if not node:
                return
            if not node.left and newRoot == None:
                #since we're doing inorder traversal, the first left leaf
                #that we see will be the new root
                newRoot = node
            dfs(node.left, True, node, node.right)
            dfs(node.right, False, node, None)
            if isLeft:
                #the left child is responsible for setting itself up
                node.left = parent_right
                node.right = parent
            else:
                #remove any links
                node.left = None
                node.right = None

        dfs(root, False, None, None)
        return newRoot