# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        cnt = 0
        tmp = head
        while tmp:
            cnt+=1
            tmp = tmp.next
        
        def reverse(node):
            if not node:
                return
            tmp = node
            prev = None
            fwd = None
            while tmp:
                fwd = tmp.next
                tmp.next = prev
                prev = tmp
                tmp = fwd
            return prev
        def compare(a, b):
            while a and b:
                if a.val != b.val:
                    return False
                a = a.next
                b = b.next
            return True
        
        mid_ptr = head
        prev = None
        for i in range(cnt//2):
            mid_ptr = mid_ptr.next

        ptr = reverse(mid_ptr)
        return compare(head, ptr)



        