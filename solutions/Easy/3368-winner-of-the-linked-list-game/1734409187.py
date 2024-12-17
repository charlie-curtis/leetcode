# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:

        balance = 0
        while head:
            a = head.val
            b = head.next.val
            if b > a:
                balance-=1
            else:
                balance+=1
            head=head.next.next

        if balance == 0: return "Tie"
        if balance < 0: return "Odd"
        return "Even"
        