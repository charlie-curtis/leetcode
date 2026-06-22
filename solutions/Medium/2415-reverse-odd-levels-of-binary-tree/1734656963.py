# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        d = defaultdict(list)

        def dfs(node, lvl, isRead):
            if not node:
                return
            if lvl % 2 == 1:
                if isRead:
                    d[lvl].append(node.val)
                else:
                    node.val = d[lvl].pop()
            
            dfs(node.left, lvl+1, isRead)
            dfs(node.right, lvl+1, isRead)


        dfs(root, 0, True)
        dfs(root, 0, False)
        return root




        