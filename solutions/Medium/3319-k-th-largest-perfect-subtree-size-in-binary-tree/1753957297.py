# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        sizes=[]

        def dfs(node):
            if not node:
                return [True,0,0]
            isLeaf= not node.left and not node.right
            if isLeaf:
                sizes.append(1)
                return [True,1,1]
            #good,depth,size
            L = dfs(node.left)
            R = dfs(node.right)
            good=L[0] and R[0] and L[1] == R[1]
            if good:
                sizes.append(L[2]*2+1)
            return [
                good,
                L[1]+1,
                L[2]*2 +1,
            ]
        dfs(root)
        sizes.sort()
        print(sizes)
        return sizes[-k] if len(sizes) >= k else -1
            
        