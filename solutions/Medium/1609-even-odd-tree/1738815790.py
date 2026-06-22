# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:


        d = defaultdict(list)
        def dfs(node,depth):
            if not node:
                return

            d[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)


        dfs(root, 0)
        if not d.keys():
            return True

        for i in range(0, max(d.keys())+1):
            if len(set(d[i])) != len(d[i]):
                return False
            if i % 2 == 0:
                expected = sorted(d[i])
                if not all([x%2 == 1 for x in d[i]]):
                    return False
            else:
                expected = sorted(d[i])[::-1]
                if not all([x%2 == 0 for x in d[i]]):
                    return False

            if d[i] != expected:
                return False
        return True
            
        