# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        def dfs(node):
            isLeaf = not node.left and not node.right

            if isLeaf:
                ans.append(node.val)
                return True
            
            if node.left:
                res = dfs(node.left)
                if res:
                    node.left = None
            if node.right:
                res = dfs(node.right)
                if res:
                    node.right = None
            return False


        out = []
        while root.left or root.right:
            dfs(root)
            out.append(ans.copy())
            ans = []
        
        out.append([root.val])

        return out

        