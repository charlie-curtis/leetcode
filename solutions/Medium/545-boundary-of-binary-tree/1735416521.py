# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        lefts = []
        rights = []
        leaves = []

        def dfs_leaves(cur):
            if not cur:
                return
            isLeaf = cur.left == None and cur.right == None

            if isLeaf:
                leaves.append(cur.val)
            
            dfs_leaves(cur.left)
            dfs_leaves(cur.right)

        dfs_leaves(root)

        def dfs_left(cur):
            if cur.left == None and cur.right == None:
                return

            lefts.append(cur.val)
            if cur.left:
                dfs_left(cur.left)
            elif cur.right:
                dfs_left(cur.right)

        def dfs_right(cur):
            if cur.left == None and cur.right == None:
                return
            rights.append(cur.val)
            if cur.right:
                dfs_right(cur.right)
            elif cur.left:
                dfs_right(cur.left)

        if root.left:
            dfs_left(root.left)
        if root.right:
            dfs_right(root.right)

        ans = [root.val]
        if lefts:
            ans+=lefts
        if leaves:
            ans+=leaves
        if rights:
            ans+= rights[::-1]
        return ans




        