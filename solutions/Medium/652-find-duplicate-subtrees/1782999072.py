# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        d = defaultdict(int)
        ans = []

        def dfs(node):
            if not node:
                return hash(None)
            
            L = dfs(node.left)
            R = dfs(node.right)

            me = hash((L, R, node.val, abs(node.val)))
            d[me]+=1
            if me == 5800372942282918319:
                print("HIT", node)
            if d[me] == 2:
                ans.append(node)
            return me
        
        dfs(root)
        return ans
        