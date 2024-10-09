# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:


        sums = []
        def dfs(node):

            if not node: return 0

            me = node.val
            l = dfs(node.left)
            r = dfs(node.right)

            sums.append(me+l+r)
            return sums[-1]

        dfs(root)
        t = sums.pop()
        return t/2 in sums


