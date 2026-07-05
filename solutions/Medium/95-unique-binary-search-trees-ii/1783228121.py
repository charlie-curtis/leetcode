# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:


        def bt(start, stop):
            if stop < start:
                return [None]
            if start == stop:
                return [TreeNode(start)]

            out = []
            for i in range(start, stop+1):
                #assume i is the root
                lefts = bt(start, i-1)
                rights = bt(i+1, stop)

                for left_node in lefts:
                    for right_node in rights:
                        me = TreeNode(i)
                        me.left = left_node
                        me.right = right_node
                        out.append(me)
            return out

        
        return bt(1, n)