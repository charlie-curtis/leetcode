# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:

        A = [0]
        B = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isnumeric():
                j = i
                while j < n and s[j].isnumeric():
                    j+=1
                B.append(int(s[i:j]))
                i = j
            else:
                j = i
                while j < n and not s[j].isnumeric():
                    j+=1
                A.append(j-i)
                i=j

        A = list(zip(A,B))

        n = len(A)
        def dfs(i, d):
            node = None
            if i < n and A[i][0] == d:
                node = TreeNode(A[i][1])
            if i+1 < n and A[i+1][0] == d+1:
                #print("HIT")
                left, i = dfs(i+1, d+1)
                node.left = left
            if i+1 < n and A[i+1][0] == d+1:
                #print("HIT2")
                right, i = dfs(i+1, d+1)
                node.right = right
            return [node, i]
        
        return dfs(0, 0)[0]

            


