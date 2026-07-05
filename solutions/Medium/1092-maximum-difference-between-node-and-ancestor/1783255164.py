# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:


        ans=0
        def dfs(node):
            if not node:
                return [10**9, -10**9]
            llow,lhigh = dfs(node.left)
            rlow,rhigh = dfs(node.right)
            low = min(llow,rlow)
            high = max(lhigh,rhigh)
            nonlocal ans
            ans=max(node.val- low,max(ans, high-node.val))
            return [min(low, node.val), max(high, node.val)]

        dfs(root)
        return ans
        