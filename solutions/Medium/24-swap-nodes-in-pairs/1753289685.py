# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def do(node):
            swapped = None
            if node and node.next:
                swapped = do(node.next.next)
            
            if node and node.next:
                fwd = node.next
                back = node
                back.next = swapped
                fwd.next = back
                return fwd
            return node
        return do(head)