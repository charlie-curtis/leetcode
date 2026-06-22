# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        A = []
        while head:
            A.append(head.val)
            head = head.next
        found = True
        while found:
            ssum = 0
            H = {}
            H[0] = -1
            found = False
            for i,x in enumerate(A):
                ssum+=x
                if ssum in H:
                    found = True
                    j = H[ssum]
                    A = A[0:j+1] + A[i+1:]
                    break
                else:
                    H[ssum] = i
        fakeHead = ListNode(-1)
        t = fakeHead
        for x in A:
            node = ListNode(x)
            t.next = node
            t = node
        return fakeHead.next
