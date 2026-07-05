# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:


        cnt = 0
        active = False 
        while head != None:
            v = head.val
            if v in nums and not active:
                #we have to "pay" to turn the activate flag to True
                cnt+=1
            
            active = v in nums
            head = head.next
        
        return cnt
        