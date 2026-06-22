# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def count(li):
            goal = sorted(li)
            actual_pos = defaultdict(int)
            for i,x in enumerate(li):
                actual_pos[x] = i
            
            ans = 0
            m = len(li)
            for i in range(m):
                v = goal[i]
                j = actual_pos[v]
                if i == j:
                    continue
                else:
                    ans+=1
                    li[i], li[j] = li[j], li[i]
                    actual_pos[li[i]] = i
                    actual_pos[li[j]] = j

            return ans
                

        d = defaultdict(list)
        def dfs(root, lvl):
            if not root:
                return

            d[lvl].append(root.val)
            dfs(root.left, lvl+1)
            dfs(root.right, lvl+1)



        dfs(root, 0)
        mmax = max(d.keys())
        ans = 0
        for i in range(mmax+1):
            res = count(d[i])
            ans+=res
        return ans



        