# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:


        def count(node):
            cnt = 0
            while node != None:
                cnt+=1
                node = node.next
            return cnt

        def rev(cur):
            prev = None
            while cur != None:
                cur.next, prev, cur = prev, cur, cur.next
            return prev
        
        n = count(head)

        node = head
        prev = None
        for i in range(n//2):
            prev = node
            node = node.next
        
        prev.next = None

        node = rev(node)
        best = 0
        for i in range(n//2):
            best = max(best, node.val + head.val)
            head = head.next
            node = node.next
        return best
