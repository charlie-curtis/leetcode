# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        
        d = defaultdict(list)
        
        def dfs(cur, i):
            
            if not cur:
                return
            
            d[i].append(cur.val)
            dfs(cur.left, i+1)
            dfs(cur.right, i+1)
            
        dfs(root, 0)
        
        mmax = max(d.keys())
        return [max(d[i]) for i in range(mmax+1)]

            
        