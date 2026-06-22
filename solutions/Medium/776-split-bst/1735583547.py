# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:

        #I looked at the editorial for the approach. With great difficulty, I originally got this question on my own, but it was like 100 lines of unreadable code
        def dfs(node):
            if not node:
                return [None, None]

            LL, HL = dfs(node.left)
            LR, HR = dfs(node.right)

            if node.val <= target:
                #I'm in the lower tree
                node.right = LR
                res = [node, HR]
            else:
                #I'm in the higher tree
                node.left = HL
                res = [LL, node]
            return res

        return dfs(root)