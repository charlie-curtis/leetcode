# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        originalA = headA
        originalB = headB
        while headA != headB:
            if not headA:
                headA = originalB
            else:
                headA = headA.next
            if not headB:
                headB = originalA
            else:
                headB = headB.next
            
        #Note the above algo will terminate after the second loop because they'll both reach the end at the same time (and be null if)
        return headA