# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        ans = None
        flag = False
        def dfs(node):
            nonlocal ans, flag
            if not node or ans:
                return

            skip = not flag and node.val < p.val
            if not skip:
                dfs(node.left)
            if flag and not ans:
                ans = node
            elif node == p:
                flag = True
            dfs(node.right)
        
        dfs(root)
        return ans
        