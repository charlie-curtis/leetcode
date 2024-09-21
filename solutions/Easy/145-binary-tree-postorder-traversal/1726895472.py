# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def go(node):
            if not node:
                return
            go(node.left)
            go(node.right)
            ans.append(node.val)
        go(root)
        return ans
        
        