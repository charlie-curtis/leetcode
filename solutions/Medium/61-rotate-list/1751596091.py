# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 0 or not head:
            return head
        def count(head):
            tmp = head
            cnt = 0
            while tmp:
                cnt+=1
                tmp = tmp.next
            return cnt

        n = count(head)
        k%=n

        if k == 0:
            return head
        
        #k > 0

        #so if k = 2, we take the last 2 nodes from the end and put it at the beginning

        move = n-k

        front = head
        back = None
        while move:
            back = front
            front = front.next
            move-=1
        back.next = None
        newhead = front
        while front:
            back = front
            front=front.next
        back.next = head



        return newhead
        