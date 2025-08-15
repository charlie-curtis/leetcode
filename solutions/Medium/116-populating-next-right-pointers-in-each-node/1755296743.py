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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        q = deque()
        q.append(root)

        if not root:
            return root

        while q:
            last = None
            for _ in range(len(q)):
                cur = q.pop()
                cur.next = last
                last = cur
                if cur.right:
                    q.appendleft(cur.right)
                if cur.left:
                    q.appendleft(cur.left)
        return root


