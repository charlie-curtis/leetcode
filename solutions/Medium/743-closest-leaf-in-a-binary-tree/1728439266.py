# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NewNode:
    def __init__(self, val=0, left=None, right=None, prev=None):
        self.val = val
        self.left = left
        self.right = right
        self.prev = prev
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:


        start = None
        d = {}
        def dfs(node, prev):
            if not node:
                return None

            newNode = NewNode(node.val)
            newNode.left = dfs(node.left, newNode)
            newNode.right = dfs(node.right, newNode)
            newNode.prev = prev

            d[node.val] = newNode
            return newNode

        dfs(root, None)


        seen = set()
        q = deque()
        q.append(k)
        seen.add(k)


        while q:
            cur = q.popleft()
            node = d[cur]
            if not node.left and not node.right:
                return node.val 
            
            if node.left and node.left.val not in seen:
                seen.add(node.left.val)
                q.append(node.left.val)
            if node.right and node.right.val not in seen:
                seen.add(node.right.val)
                q.append(node.right.val)
            if node.prev and node.prev.val not in seen:
                seen.add(node.prev.val)
                q.append(node.prev.val)

        