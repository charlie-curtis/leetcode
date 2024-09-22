# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        ans = 1e10

        def go(node):
            nonlocal ans
            if not node:
                return
            dst = abs(node.val - target)
            best = abs(ans-target)
            if dst == 0:
                ans = node.val
                return

            if dst < best or (dst == best and node.val < ans):
                ans = node.val

            if node.val > target:
                go(node.left)
            else:
                go(node.right)
            
        go(root)
        return ans
        