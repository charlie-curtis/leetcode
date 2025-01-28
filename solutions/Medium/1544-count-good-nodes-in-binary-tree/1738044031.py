# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = 0
        def dfs(cur, prev):
            if not cur:
                return

            if cur.val >= prev:
                nonlocal ans
                ans+=1

            prev = max(cur.val,prev)
            dfs(cur.left, prev)
            dfs(cur.right, prev)

        dfs(root, -1e15)
        return ans
        