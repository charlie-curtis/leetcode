# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0


        d = defaultdict(int)
        def dfs(node, depth):
            if not node:
                return 

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            d[depth]+=node.val

        dfs(root, 1)

        best = d[1] 
        lvl = 1
        mmax = max(d.keys())
        for i in range(2,mmax+1):
            if d[i] < best:
                lvl = i
                best = d[i]
        return lvl


        