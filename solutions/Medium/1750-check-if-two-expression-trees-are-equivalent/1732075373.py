# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:


        def doSum(node):
            if not node:
                return []

            l = doSum(node.left)
            r = doSum(node.right)


            res = []
            if node.val != '+':
                res.append(node.val)
            else:
                res+= l
                res+= r


            return res



        a = sorted(doSum(root1))
        b = sorted(doSum(root2))
        return a == b

        