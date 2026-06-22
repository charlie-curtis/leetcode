# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        C = Counter()

        def isgood():
            ans = 0
            for x in C.values():
                if x % 2 == 1:
                    ans+=1
            return ans <= 1

        ans = 0
        def dfs(cur):
            if not cur:
                return
            C[cur.val]+=1
            isLeaf = cur.left == None and cur.right == None
            if isLeaf:
                if isgood():
                    nonlocal ans
                    ans+=1
            else:
                dfs(cur.left)
                dfs(cur.right)
            C[cur.val]-=1

        dfs(root)
        return ans