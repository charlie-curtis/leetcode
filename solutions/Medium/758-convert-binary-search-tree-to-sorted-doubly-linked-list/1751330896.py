"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':


        #inorder traversal
        if not root:
            return  root

        head = end = prev = -1
        def dfs(node):
            nonlocal prev, head,end
            if not node:
                return


            l = dfs(node.left)
            if head == -1:
                head = node
            end = node
            if prev != -1:
                prev.right = node
                node.left = prev

            prev = node
            dfs(node.right)


        dfs(root)
        end.right = head
        head.left = end

        return head
            




        