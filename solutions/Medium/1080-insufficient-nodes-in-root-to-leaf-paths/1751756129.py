# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:


        def dfs(node, ssum):
            if not node:
                return False
            ssum+=node.val
            if not node.left and not node.right:
                #leaf
                return ssum >= limit
            
            L = dfs(node.left, ssum)
            R = dfs(node.right, ssum)

            if not L:
                node.left = None
            if not R:
                node.right = None

            return L or R
        
        res = dfs(root, 0)
        return root if res else None
        