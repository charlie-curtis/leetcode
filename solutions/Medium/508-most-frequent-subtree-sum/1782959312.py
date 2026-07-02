# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:


        C = Counter()

        def dfs(node):
            if not node:
                return 0
            
            a = dfs(node.right)
            b = dfs(node.left)
            c = node.val

            ssum = a + b + c
            C[ssum]+=1
            return ssum
        
        dfs(root)
        mmax = max(C.values())
        return [k for (k,v) in C.items() if v == mmax]
        