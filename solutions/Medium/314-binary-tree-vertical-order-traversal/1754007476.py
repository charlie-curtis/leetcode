# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []


        d = defaultdict(list)
        q = deque()
        q.append([root, 0])

        while q:
            node, b = q.popleft()

            d[b].append(node.val)
            if node.left:
                q.append([node.left, b-1])
            if node.right:
                q.append([node.right, b+1])

        mmin = min(d.keys())
        mmax = max(d.keys())

        ans = []
        for i in range(mmin, mmax+1):
            ans.append(d[i])
        return ans
        