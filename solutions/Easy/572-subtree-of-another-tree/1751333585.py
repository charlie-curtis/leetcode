# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def dfs(cur):
            if not cur:
                return False
            
            if dfs(cur.left):
                return True
            if dfs(cur.right):
                return True
            if check(cur, subRoot):
                return True
            return False
        
        def check(p, q):
            if not p or not q:
                return p == q
            
            r = check(p.right, q.right)
            if not r:
                return False
            l = check(p.left, q.left)
            if not l:
                return False
            return p.val == q.val


        return dfs(root)
        