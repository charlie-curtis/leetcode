# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        def getRoute(node, target, route):
            if not node:
                return False

            route.add(node.val)
            l = getRoute(node.left, target, route)
            r = getRoute(node.right, target, route)

            found = l or r or target == node.val
            if not found:
                #if we found it on our path, then don't remove 
                route.remove(node.val)

            return found

        
        a = set()
        b = set()
        tmp = root
        getRoute(root, p, a)
        getRoute(tmp, q, b)

        overlap = len(a&b)


        #either way works. Either A xor B or add both set sizes together, and remove the common parts
        #return len(a) + len(b) - 2*overlap

        return len(a^b)

            


        