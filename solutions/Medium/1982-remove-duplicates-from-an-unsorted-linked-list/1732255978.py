# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:


        C = Counter()

        tmp = head
        while tmp:
            C[tmp.val]+=1
            tmp = tmp.next
        
        fakeHead = ListNode(-1)
        endNode = fakeHead
        tmp = head
        while tmp:
            if C[tmp.val] == 1:
                endNode.next = tmp
                endNode = endNode.next
                tmp = tmp.next
                endNode.next = None
            else:
                tmp = tmp.next


        return fakeHead.next