# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:

        ans = head
        while head:
            i = 0
            prev = None
            while head and i < m:
                i+=1
                prev = head
                head = head.next
            
            i = 0
            while head and i < n:
                i+=1
                head = head.next
            prev.next = head
        
        return ans