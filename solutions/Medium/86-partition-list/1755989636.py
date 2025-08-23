# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        le = ListNode(-1)
        gte = ListNode(-1)
        o = le
        o1 = gte

        while head:
            nxt = head.next
            head.next = None
            if head.val < x:
                le.next = head
                le = le.next
            else:
                gte.next = head
                gte = gte.next
            head = nxt
        
        
        if o1.next and o.next:
            le.next = o1.next
            return o.next
        if o.next:
            return o.next
        return o1.next