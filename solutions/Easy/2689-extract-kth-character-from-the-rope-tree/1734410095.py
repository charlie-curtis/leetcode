# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """


        out = ""
        def dfs(node):
            nonlocal out
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            if node.val:
                out+=node.val

        dfs(root)
        return out[k-1]
        