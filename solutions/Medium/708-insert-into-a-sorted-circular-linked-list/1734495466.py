"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        def inspect(low, high):
            t = head
            C = Counter()
            is_outside = insertVal < low or insertVal > high
            while C[head] < 2:
                C[t]+=1
                fwd = t.next
                if (t.val <= insertVal <= fwd.val) or (is_outside and t.val == high and t.next.val != high):
                    node = Node(insertVal)
                    t.next = node
                    node.next = fwd
                    return
                t = t.next

        def getMinMax(head):
            t = head
            high = -1e15
            low = 1e15
            C = Counter()
            while C[head] < 2:
                high = max(high, t.val)
                low = min(low, t.val)
                C[t]+=1
                t = t.next
            return [low, high]

        #case 1. There isn't a head
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        #case 2. all the nodes have the same value
        low, high = getMinMax(head)
        if low == high:
            new = Node(insertVal)
            t = head.next
            head.next = new
            new.next = t
            return head
        
        #case 3. The value is either inside our range or outside our range.
        inspect(low, high)

        return head

        