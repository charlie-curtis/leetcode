# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:


        ans = 0
        def find(node):
            nonlocal ans
            if not node:
                return [-1,-1,0]
            
            llow, lhigh, lsz = find(node.left)
            rlow, rhigh, rsz = find(node.right)

            if lsz == -1 or rsz == -1:
                return [0, 0, -1]

            if lsz > 0:#need to validate
                
                if lhigh >= node.val:
                    return [0, 0, -1]
            if rsz > 0:#need to validate
                if node.val >= rlow:
                    return [0,0, -1]
            
            high = rhigh if rhigh != -1 else node.val
            low = llow if llow != -1 else node.val
            can = lsz + rsz + 1
            ans = max(can, ans)
            return [low,high, can]

        find(root)
        return ans


        