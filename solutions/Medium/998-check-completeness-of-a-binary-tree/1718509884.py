# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:



        queue = deque()
        queue.append(root)

        A = []
        while queue:

            node = queue.popleft()

            if node == None:
                continue

            l = node.left if node else None
            r = node.right if node else None
            A.append(l)
            A.append(r)
            queue.append(l)
            queue.append(r)


        seen = False
        for i,x in enumerate(A):
            if x == None:
                seen = True
            elif x != None and seen:
                return False
        return True

