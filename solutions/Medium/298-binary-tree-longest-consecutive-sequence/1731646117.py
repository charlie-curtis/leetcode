# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:



        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            
            l = dfs(node.left) 
            r = dfs(node.right)

            if node.left and node.left.val - node.val == 1:
                l+=1
            else:
                l = 1
            if node.right and node.right.val - node.val == 1:
                r+=1
            else:
                r=1

            ans = max(ans, max(l,r))

            return max(l,r)

        dfs(root)
        return ans

        