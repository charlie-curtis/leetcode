# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:

        d = defaultdict(set)
        parents = {}

        def dfs(node, depth):

            if not node:
                return

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

            d[depth].add(node)
            if node.left:
                parents[node.left] = node
            if node.right:
                parents[node.right] = node

        dfs(root, 0)

        mmax = max(d.keys())

        bad = None
        for i in range(1,mmax+1):
            if bad:
                break

            #d[i] is all the nodes at depth i
            for x in d[i]:
                if x.right in d[i]:
                    bad = x
                    break
                

        bad_parent = parents[bad]
        if bad_parent.left == bad:
            bad_parent.left = None
        else:
            bad_parent.right = None

        return root
