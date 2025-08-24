# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odds = ListNode(-1)
        evens = ListNode(-1)

        o = odds
        o1 = evens

        cnt = 0
        while head:
            cnt+=1
            if cnt % 2:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            nxt = head.next
            head.next = None
            head = nxt
        
        if cnt == 1:
            return o.next
        else:
            odds.next = o1.next
            return o.next
        