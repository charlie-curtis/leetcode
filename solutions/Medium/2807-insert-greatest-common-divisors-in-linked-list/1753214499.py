# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmp = head
        b = None
        while tmp:
            b = tmp
            tmp=tmp.next
            if tmp:
                node = ListNode(gcd(b.val, tmp.val))
                b.next = node
                node.next = tmp
                b = b.next

        return head
        