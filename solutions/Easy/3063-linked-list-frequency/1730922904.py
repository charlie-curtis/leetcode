# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:

        C = Counter()

        while head:
            C[head.val]+=1
            head = head.next

        fakeHead = ListNode()
        cur = fakeHead
        for x in C.values():
            cur.next = ListNode(x)
            cur = cur.next
        return fakeHead.next
        