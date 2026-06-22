# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def count(head):
            t=head
            i=0
            while t:
                i+=1
                t=t.next
            return i
        n=count(head)
        if n==1:return None
        if n==2:
            head.next=None
            return head
        fwd=head
        back=None
        t=n//2
        while t:
            t-=1
            back=fwd
            fwd=fwd.next
        back.next=fwd.next
        return head