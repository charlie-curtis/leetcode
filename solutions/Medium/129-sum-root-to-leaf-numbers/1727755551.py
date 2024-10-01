# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:


        ans = 0
        def dfs(node, ssum):
            nonlocal ans
            if not node:
                return
            ssum= ssum*10 + node.val
            if not node.left and not node.right:
                ans+=ssum
            
            dfs(node.left, ssum)
            dfs(node.right, ssum)
        
        dfs(root, 0)
        return ans
        