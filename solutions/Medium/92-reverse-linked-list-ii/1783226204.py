# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:


        def rev(node, cnt):
            prev = None
            original = node

            i = 0
            for i in range(cnt):
                fwd = node.next

                node.next = prev
                prev = node
                node = fwd
                i+=1
            original.next = fwd
            return prev

        
        cnt = 0
        node = head
        prev = None
        while cnt <= right:
            cnt+=1
            fwd = node.next
            if cnt == left:
                front = rev(node, right-left+1)
                if prev:
                    prev.next = front
                break
            prev = node
            node = node.next
        
        return front if left == 1 else head
        