# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def count(node):
            cnt = 0
            while node != None:
                cnt+=1
                node = node.next
            return cnt


        def rev(node, cnt):

            prev = None
            first = node
            #1 -> 2 -> 3 | -> 4
            for i in range(cnt):
                fwd = node.next
                node.next = prev
                prev = node
                node = fwd
            first.next = node # connect 1 to 4
            return prev

        
        #12
        #1,2,3,4,2
        i = 0
        n = count(head)
        node = head
        expected_size = 0
        prev = None
        while i < n:
            #get size
            expected_size+=1
            actual = min(n-i, expected_size)

            #if even, reverse
            if actual % 2 == 0:
                node = rev(node, actual)
                if prev:
                    prev.next = node
                else:
                    head = node
            #advance the pointer
            for _ in range(actual):
                prev = node
                node = node.next
            i+=actual
        
        return head


        