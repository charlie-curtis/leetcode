# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        if not s:
            return None
        
        def dfs(cur):

            v = ""
            while cur and cur[0] != "(" and cur[0] != ")":
                v+=cur.popleft()
            node = TreeNode(int(v))
            if cur and cur[0] == '(':
                cur.popleft()
                node.left = dfs(cur)
                cur.popleft()
            
            if cur and cur[0] == ')':
                return node


            if cur and cur[0] == '(':
                cur.popleft()
                node.right = dfs(cur)
                cur.popleft()

            if cur and cur[0] == ')':
                return node
            
            return node


        return dfs(deque([x for x in s]))

        