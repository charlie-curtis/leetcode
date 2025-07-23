# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        def count(node):
            cnt = 0
            while node:
                cnt+=1
                node = node.next
            return cnt

        def pprint(x):
            A = []
            while x:
                A.append(x.val)
                x = x.next
            print("Printing:", A)

        n = count(head)
        if n == 0:
            return None
        
        times = n//k

        res = None 
        cur = head
        fakeHead = ListNode(-1)
        prev = fakeHead
        for i in range(times):

            #reverse the nodes, and then make sure the endpoints are connected properly
            #prev = previous group
            #cur = start of new group before reversing
            back = None
            first = cur
            for j in range(k):
                fwd = cur.next
                cur.next = back
                back = cur
                cur = fwd
            #done with the reverse, now hook in the right stuff
            #back is now pointing to the new front, so connect those

            #tie the previous group to this group
            prev.next = back
            #tie this group to the next one
            first.next = cur

            #setup for the next group. prev is now the original first
            prev = first
            #cur is already set

        #loop broke. There might be some unhandled nodes
        return fakeHead.next