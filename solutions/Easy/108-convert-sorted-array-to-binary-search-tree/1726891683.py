# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def go(start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(nums[start])
            
            mid = start + (end-start)//2
            head = TreeNode(nums[mid])
            head.left = go(start,mid-1)
            head.right = go(mid+1, end)
            return head
        return go(0, len(nums)-1)

        