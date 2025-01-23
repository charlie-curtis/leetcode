# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:


        @cache
        def dfs2(node, isLeft):
            if not node:
                return 0

            if isLeft == -1:
                return 1 + max(dfs2(node.left, True), dfs2(node.right, False))
            if isLeft == True:
                return 1 + dfs2(node.right, False)
            else:
                return 1 + dfs2(node.left, True)


        ans = 0

        def dfs(node):
            if not node:
                return

            nonlocal ans
            ans = max(ans, dfs2(node, -1))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans-1