# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':

        if not root:
            return root

        d = {}

        def dfs(node):
            if not node:
                return None
            
            l = dfs(node.left)
            r = dfs(node.right)

            me = NodeCopy(node.val)
            me.left = l
            me.right = r
            d[node] = me
            return me

        dfs(root)

        def dfs2(node):
            if not node:
                return
            
            cloned = d[node]
            old_random = node.random
            if old_random in d:
                cloned.random = d[old_random]
            dfs2(node.left)
            dfs2(node.right)

        
        dfs2(root)

        return d[root]