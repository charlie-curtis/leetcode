# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        #cases:
        #1. node not found -> do nothing
        #2. node is found, node has 2 no children -> just delete it
        #3. node is found, node has only left child -> just promote it
        #4. node is found, node has only right child -> just promote it
        #5. node is found, has both left & right child ->
            #promote right child
            #child's left subtree gets pushed down as far as possible
            #into the right of the deleted node's left subtree
        
        def update(node):
            if not node:
                return None
            if key == node.val:
                #this is our moment

                #case2
                if not node.left and not node.right: return None
                #case3
                if node.left and not node.right: return node.left
                #case4
                if node.right and not node.left: return node.right
                #case5
                #the promoted nodes sibling becomes the old left
                tmp = node.right.left
                node.right.left = node.left

                #we have a dangling tmp that we now have to put somewhere, so shove it as far right in
                #the deleted nodes left subtree as possible
                t = node.left
                while t.right:
                    t = t.right
                t.right = tmp
                #promote the node
                return node.right

            elif key > node.val:
                node.right = update(node.right)
            else:
                node.left = update(node.left)
            return node
        
        res = update(root)
        return res

        