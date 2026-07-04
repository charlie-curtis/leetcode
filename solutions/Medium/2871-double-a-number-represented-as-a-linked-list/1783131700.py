# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rev(tmp):
            node = tmp

            prev = None
            while node != None:
                fwd = node.next
                node.next = prev
                prev = node
                node = fwd
            return prev
        
        def double(tmp):
            node = tmp
            carry = 0
            prev = None
            while node != None:
                prev = node
                node.val = node.val*2 + carry
                carry = node.val // 10
                node.val = node.val % 10
                node = node.next

            if carry:
                prev.next = ListNode(carry)

        h = rev(head)
        double(h)
        return rev(h)
        