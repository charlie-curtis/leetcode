"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:

        if not node:
            return []
        d = deque()
        d.append(node.val)

        fwd = node.next
        prev = node.prev
        while fwd != None:
            d.append(fwd.val)
            fwd = fwd.next

        while prev != None:
            d.appendleft(prev.val)
            prev = prev.prev
        return d
        



        