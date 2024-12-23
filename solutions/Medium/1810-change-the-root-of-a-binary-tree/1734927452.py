"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':


        def do(node, prev):
            if not node:
                return 

            #do some special stuff for root
            if node.left and node.left != prev and node != root:
                node.right = node.left

            if node == root:
                if node.right == prev:
                    node.right = None
                else:
                    node.left = None
                node.parent = prev
                return
            
            node.left = node.parent
            p = node.parent
            node.parent = prev
            do(p, node)

        do(leaf, None)
        return leaf