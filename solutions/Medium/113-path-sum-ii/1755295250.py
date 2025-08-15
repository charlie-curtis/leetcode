# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        ans = []
        def dfs(node, cur, ssum):

            isLeaf = not node.right and not node.left

            cur.append(node.val)
            ssum+=node.val

            if isLeaf:
                if ssum == targetSum:
                    ans.append(cur.copy())
            else:
                if node.left:
                    dfs(node.left, cur, ssum)
                if node.right:
                    dfs(node.right, cur, ssum)
            cur.pop()
        dfs(root, [], 0)
        return ans

        