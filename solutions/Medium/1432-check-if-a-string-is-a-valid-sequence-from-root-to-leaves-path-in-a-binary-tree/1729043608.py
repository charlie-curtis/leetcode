# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:

        def dfs(node, i):

            if not node:
                return False

            good = node.val == arr[i]
            if not good: return False

            isLeaf = not node.left and not node.right
            if i+1 == len(arr): return isLeaf

            a = dfs(node.left, i+1)
            b = dfs(node.right, i+1)
            return a or b

        return dfs(root, 0)

        