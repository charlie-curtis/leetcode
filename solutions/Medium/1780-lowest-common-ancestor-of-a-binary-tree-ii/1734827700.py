# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        ans = None
        def solve(node):
            nonlocal ans
            if not node:
                return 0

            l = solve(node.left)
            r = solve(node.right)

            cnt = l + r
            if cnt == 2 and ans == None:
                #my left found a node, my right found a node, and ans isn't set yet, so i'm the LCA
                ans = node
            elif cnt == 1 and (node.val == p.val or node.val == q.val):
                #either my left or right found a node, and I found the other, so i'm the LCA
                ans = node

            return cnt + (1 if node.val == p.val or node.val == q.val else 0)
            


        solve(root)
        return ans
        