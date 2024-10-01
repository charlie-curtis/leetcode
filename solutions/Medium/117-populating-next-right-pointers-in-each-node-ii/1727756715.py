"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None
        d = {}
        q = deque()
        q.append([root, 0])
        while q:
            node, lvl = q.popleft()
            if lvl in d:
                node.next = d[lvl]

            d[lvl] = node
            
            if node.right:
                q.append([node.right, lvl+1])
            if node.left:
                q.append([node.left, lvl+1])
        return root
        