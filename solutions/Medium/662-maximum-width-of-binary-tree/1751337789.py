# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append([root, 0])
        ans = 0

        
        while q:
            _, small = q[0]
            for i in range(len(q)):
                node, pos = q.popleft()
                if node.left:
                    q.append([node.left, 2*pos])
                if node.right:
                    q.append([node.right, 2*pos+1])
            ans = max(ans, abs(pos - small))
        return ans + 1
            

        