# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        dp_do = Counter()
        dp_dont = Counter()

        def dfs(node, i):

            if not node:
                return
            
            dfs(node.left, 2*i)
            dfs(node.right, 2*i + 1)

            dp_dont[i] = dp_do[2*i] + dp_do[2*i+1]
            dp_do[i] = node.val + dp_dont[2*i] + dp_dont[2*i+1]
            dp_do[i] = max(dp_do[i], dp_dont[i])

        dfs(root, 1)
        return max(dp_do[1], dp_dont[1])


        