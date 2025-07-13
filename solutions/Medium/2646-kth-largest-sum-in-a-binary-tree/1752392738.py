# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        C=Counter()

        def dfs(node,depth):
            if not node:return
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            C[depth]+=node.val

        dfs(root,1)
        if len(C.keys()) < k: return -1
        A=sorted(C.values())
        return A[-k]