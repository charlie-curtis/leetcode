# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, start: Optional[ListNode]) -> List[Optional[ListNode]]:

        def countNodes(start):
            n = 1
            tmp = start.next
            while start != tmp:
                tmp = tmp.next
                n+=1
            return n

        n = countNodes(start)

        tmp = start
        for i in range((n+1)//2 - 1):
            tmp = tmp.next
        
        tmp2 = tmp
        tmp = tmp.next
        tmp2.next = start

        head2 = tmp
        while tmp.next != start:
            tmp = tmp.next
        tmp.next = head2

        return [start,head2]