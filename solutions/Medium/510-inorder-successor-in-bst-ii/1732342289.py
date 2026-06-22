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
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':

        can = None

        tmp = node
        v = node.val

        if tmp.right:
            tmp = tmp.right
            while tmp and tmp.left:
                tmp = tmp.left

            can = tmp
            return can

        
        while node:
            if node.val > v:
                if can == None or node.val - v < can.val - v:
                    can = node
                break
            node = node.parent

        return can
        