# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        #return values = [# of paths, curSum]
        def dfs(node, ssum, C):
            if not node:
                return 0

            ssum+=node.val
            ans = C[ssum-targetSum]
            C[ssum]+=1
            ans+=dfs(node.left, ssum, C)
            ans+=dfs(node.right, ssum, C)
            C[ssum]-=1
            return ans

        
        C = Counter({0: 1})
        return dfs(root, 0, C)

        