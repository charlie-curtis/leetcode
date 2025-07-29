# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        ordered = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ordered.append(node.val)
            dfs(node.right)
        
        dfs(root)

        def compute(i,j):
            return max(abs(ordered[i] - target), abs(ordered[j] - target))

        n = len(ordered)
        best, best_range = 1e10, []
        j = 0
        for i in range(n):
            if i-j+1 > k:
                j+=1
            if i-j+1 == k:
                candidate = compute(i,j)
                if candidate < best:
                    best = candidate
                    best_range = [j, i]

        j, i = best_range
        return ordered[j:i+1]