# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:


        #this is the second way I wrote this function after looking at the editorial. I got it the first time using DP
        #but it was a bit unnecessary because you don't need to cache the node results -- just traverse the tree once
        def dfs(node):
            if not node:
                return [1e15,1e15]
            isLeaf = node.left == None and node.right == None
            if isLeaf:
                #cost to be true, cost to be false
                return [0,1] if node.val else [1,0]


            lt, lf = dfs(node.left)
            rt, rf = dfs(node.right)

            
            if node.val == 2:
                #OR
                t = min(lt, rt)
                f = lf + rf
                return [t,f]
            elif node.val == 3:
                #AND
                t = lt + rt
                f = min(lf, rf)
                return [t,f]
            elif node.val == 4:
                #XOR
                t = min(lt+ rf, lf + rt)
                f = min(lt + rt, rf + lf)
                return [t,f]
            elif node.val == 5:
                t = min(lf, rf)
                f = min(lt, rt)
                return [t,f]
            
            raise ValueError("Wrong Value")

        
        res = dfs(root)

        #res will be an array of [t,f], so just access the opposite index of what you're looking ofr
        return res[not result]

