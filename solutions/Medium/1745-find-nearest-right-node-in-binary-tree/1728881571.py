# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        ans = None
        q = deque([root])

        flag = False
        while q:

            n = len(q)
            for i in range(n):
                node = q.popleft()
                if flag == True:
                    return node
                if node == u:
                    flag = True
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag:
                break

        return None
        