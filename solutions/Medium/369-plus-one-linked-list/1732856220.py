# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        def rev(node):
            prev = None
            while node != None:
                fwd = node.next
                node.next = prev
                prev = node
                node = fwd

            return prev

        def addOne(a):
            node = a 
            carry = 1
            prev = None
            while node != None:
                ssum = (node.val + carry)
                carry = ssum // 10
                node.val = ssum  % 10
                prev =  node
                node = node.next

            if carry:
                tmp = ListNode(carry)
                prev.next = tmp
                prev = tmp



        head = rev(head)
        addOne(head)
        return rev(head)
        