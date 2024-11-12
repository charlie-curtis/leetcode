"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if not root:
            return 0

        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            total = 0
            h1 = h2 = 0
            for x in node.children:
                res = dfs(x)
                total+=res
                if res > h1:
                    h2 = h1
                    h1 = res
                elif res > h2:
                    h2 = res

            ans = max(ans, h1 + h2)
            return h1+1

        dfs(root)
        return ans

