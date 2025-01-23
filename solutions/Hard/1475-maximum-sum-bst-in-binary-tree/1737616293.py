# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:


        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return [0, 1e15, -1e15]

            ssum1, low1, high1 = dfs(node.left)
            ssum2, low2, high2 = dfs(node.right)

            if high1 < node.val < low2:
                ans = max(ans, ssum1+ssum2+node.val)
                return [ssum1 + ssum2 + node.val, min(low1, node.val), max(node.val,high2)]

            else:
                return [0, -1e15, 1e15]
        dfs(root)
        return ans
            
            
        