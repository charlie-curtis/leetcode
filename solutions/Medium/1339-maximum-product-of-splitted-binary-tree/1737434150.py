# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        # 11 * 10
        # 9 * 12

        #a*b > c*d?

        #a*b/(c*d) > 1?

        sums = []
        def dfs(node):
            nonlocal sums
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            me = node.val

            sums.append(l+r+me)
            return l+r+me
        dfs(root)
        total = sums.pop()
        sums.sort()
        A = []
        for x in sums:
            A.append((x, total-x))
        best = A[0]
        for x,y in A[1:]:
            if ((1/x)/y) *best[0]*best[1] < 1:
                best = x,y
        MOD = 10**9 + 7
        return best[0]*best[1] % MOD