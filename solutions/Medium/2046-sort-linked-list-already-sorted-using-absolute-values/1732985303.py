# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        negs = ListNode(-1)
        pos = ListNode(-1)


        p1 = negs
        p2 = pos

        while head:
            if head.val < 0:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next

            head = head.next
            p1.next = None
            p2.next = None

        def rev(head):

            prev = None
            original = head
            while head:
                fwd = head.next
                head.next = prev
                prev = head
                head = fwd
            return [prev, original]

        first,last = rev(negs.next)
        if first:
            last.next = pos.next
            return first
        else:
            return pos.next

        