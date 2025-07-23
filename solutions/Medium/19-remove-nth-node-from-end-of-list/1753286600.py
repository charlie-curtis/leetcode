# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        def count(head):
            tmp = head
            cnt = 0
            while tmp:
                tmp = tmp.next
                cnt+=1
            return cnt

        m = count(head)
        moves = m-n
        if moves == 0:
            return head.next

        tmp = head
        back = None
        while moves:
            back = tmp
            tmp = tmp.next
            moves-=1
        back.next = tmp.next
        return head
            

        