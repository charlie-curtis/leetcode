# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        
        nodes = []
        def explore(cur):
            nonlocal nodes
            if not cur:
                return

            nodes.append(cur.val)
            explore(cur.left)
            explore(cur.right)


        explore(root)
        nodes.sort()
        #print(nodes)
        
        def con(nodes):
            if len(nodes) == 0:
                return None
            if len(nodes) == 1:
                return TreeNode(nodes[0])

            mid = len(nodes)//2
            root = TreeNode(nodes[mid])
            root.left = con(nodes[:mid])
            root.right = con(nodes[mid+1:])
            return root


        return con(nodes)
        