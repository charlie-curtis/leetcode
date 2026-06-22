# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, dest: int) -> str:

        nei = defaultdict(list)

        def dfs1(node):
            if not node:
                return
            
            if node.left:
                nei[node.val].append(['L', node.left.val])
                nei[node.left.val].append(['U', node.val])
                dfs1(node.left)
            if node.right:
                nei[node.val].append(['R', node.right.val])
                nei[node.right.val].append(['U', node.val])
                dfs1(node.right)

        dfs1(root)
        ans = []
        def dfs(cur, prev, I):
            if cur == dest:
                nonlocal ans
                ans = I.copy()
                return
            
            for ins,node in nei[cur]:
                if node == prev:
                    continue
                I.append(ins)
                dfs(node, cur, I)
                I.pop()
        
        dfs(start, -1, [])
        return ''.join(ans)

            