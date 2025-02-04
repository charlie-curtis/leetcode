# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:


        C = Counter()
        def dfs(node, d):
            if not node:
                return
            
            isLeaf = False
            if node.left == None and node.right == None:
                isLeaf = True
            
            if isLeaf:
                C[d]+=node.val

            
            dfs(node.left, d+1)
            dfs(node.right, d+1)

        
        dfs(root, 0)
        k = max(C.keys())
        return C[k]
        