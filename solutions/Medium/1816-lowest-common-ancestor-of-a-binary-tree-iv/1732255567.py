# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        xset = set()
        for x in nodes:
            xset.add(x.val)

        ans = None 
        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            me = 1 if node.val in xset else 0
            if l + r + me == len(xset) and ans == None:
                ans = node
            
            return l + r + me


        dfs(root)
        return ans
        