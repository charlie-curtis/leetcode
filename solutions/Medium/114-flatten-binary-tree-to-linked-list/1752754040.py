# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack=[]
        last=None
        def pre(node):
            nonlocal last
            if not node:
                return None
            stack.append(node.right)
            node.right=None
            if last:
                last.right=node
            last=node
            pre(node.left)
            node.left=None
            pre(stack.pop())
        pre(root)

        t=root
        while t:
            #print(t.val)
            t=t.right