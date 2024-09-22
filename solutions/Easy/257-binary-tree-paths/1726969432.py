# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans = []
        def go(node, cur):
            if not node:
                return
            cpy = cur.copy()
            cpy.append(str(node.val))
            if not node.left and not node.right:
                ans.append(cpy)
            else:
                go(node.left, cpy)
                go(node.right, cpy)
        
        go(root, [])
        return ['->'.join(x) for x in ans]
        