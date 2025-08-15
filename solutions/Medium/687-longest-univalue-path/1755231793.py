# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            leftSame = node.left and node.left.val == node.val
            rightSame = node.right and node.right.val == node.val
            ret = 1
            nonlocal ans
            if leftSame and rightSame:
                ret = max(l,r) + 1
                ans = max(ans, l + r)
            elif rightSame:
                ret = r + 1
                ans = max(ans, r)
            elif leftSame:
                ret = l + 1
                ans = max(ans, l)
            return ret
        dfs(root)
        return ans