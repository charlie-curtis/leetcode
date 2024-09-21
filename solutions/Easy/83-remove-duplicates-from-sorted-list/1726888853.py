# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fakeHead = ListNode(-101)

        cur = fakeHead
        while head:
            if cur.val != head.val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return fakeHead.next

        