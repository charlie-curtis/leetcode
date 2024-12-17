"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        if not root:
            return None

        def clone(node):

            new = Node(node.val)
            new.children = []
            for x in node.children:
                new.children.append(clone(x))

            return new

        return clone(root)


