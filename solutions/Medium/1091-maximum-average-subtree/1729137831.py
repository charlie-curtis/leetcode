# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return [0,0]

            left = dfs(node.left)
            right = dfs(node.right)
            cnt = left[1] + right[1] + 1
            ssum = node.val + left[0] + right[0]
            ans = max(ans, ssum/cnt)
            return [ssum, cnt]

        dfs(root)
        return ans


        