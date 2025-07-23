# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq = []
        for i,head in enumerate(lists):
            if not head:
                continue
            heapq.heappush(pq, [head.val, i])
            lists[i] = head.next
        
        cur = ListNode()
        fakeHead = cur 
        while pq:
            v, i = heapq.heappop(pq)

            cur.next = ListNode(v)
            cur = cur.next
            if lists[i]:
                heapq.heappush(pq, [lists[i].val, i])
                lists[i] = lists[i].next
        return fakeHead.next
        