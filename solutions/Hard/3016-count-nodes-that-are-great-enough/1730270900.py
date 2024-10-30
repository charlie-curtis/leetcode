from sortedcontainers import SortedList
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:

        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return []
            
            l = dfs(node.left)
            r = dfs(node.right)
            combined = sorted(l + r)
            cut = min(len(combined), k)
            combined = combined[:k]
            if len(combined) == k and (combined[-1] < node.val):
                ans+=1
            combined += [node.val]
            cut = min(len(combined), k)
            return combined
        dfs(root)
        return ans
        