# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        fakeHead = ListNode(-1)
        cur = fakeHead
        carry = 0
        while l1 or l2:
            a = 0 if not l1 else l1.val
            b = 0 if not l2 else l2.val
            ssum = (a+b+carry)
            t = ssum % 10
            carry = ssum // 10
            cur.next = ListNode(t)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            cur.next = ListNode(1)
        return fakeHead.next



        