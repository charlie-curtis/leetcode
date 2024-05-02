# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        tmp = list1
        prev = None

        for i in range(a):
            prev = tmp
            tmp = tmp.next

        prev.next = list2

        for i in range(b-a+1):
            tmp = tmp.next

        tmp2 = list2
        prev = None
        while tmp2 != None:
            prev = tmp2
            tmp2 = tmp2.next
        
        prev.next = tmp
        return list1

        
