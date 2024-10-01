# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        fakeHead = ListNode(-1)

        prev = None
        cur = head
        lastInserted = fakeHead
        while cur:
            good = True
            fwd = cur.next
            if prev and prev.val == cur.val:
                good = False
            
            if fwd and fwd.val == cur.val:
                good = False
            
            if good:
                lastInserted.next = cur
                lastInserted = lastInserted.next

            prev = cur
            cur = cur.next


        if lastInserted.next:
            lastInserted.next = None

        return fakeHead.next
        

        