# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:


        ans = 0
        def dfs(cur):
            nonlocal ans
            if not cur:
                return Counter()

            isLeaf = cur.left == None and cur.right == None
            if isLeaf:
                return Counter([0])

            L = dfs(cur.left)
            R = dfs(cur.right)
            for k1 in L.keys():
                for k2 in R.keys():
                    if k1 + k2 + 2 <= distance:
                        ans+=L[k1]*R[k2]

            out = Counter()
            for k1,v1 in (L + R).items():
                out[k1+1]+=v1
            return out


        dfs(root)
        return ans