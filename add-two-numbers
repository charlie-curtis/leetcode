#https://leetcode.com/problems/add-two-numbers/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        fake = ptr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            ssum = a + b + carry
            carry = ssum // 10
            ptr.next = ListNode(ssum % 10)
            ptr = ptr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return fake.next
