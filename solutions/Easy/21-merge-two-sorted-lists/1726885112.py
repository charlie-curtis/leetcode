# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fakeHead = ListNode(-1)

        cur = fakeHead
        while list1 or list2:
            a = list1.val if list1 else 1e10
            b = list2.val if list2 else 1e10

            if a < b:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        return fakeHead.next

        