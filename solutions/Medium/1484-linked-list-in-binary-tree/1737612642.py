# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        goal = []
        while head:
            goal.append(head.val)
            head = head.next

        #print(goal)

        k = len(goal)

        def dfs(node, path):
            #print("PATH", path)
            if not node:
                return False

            path.append(node.val)
            if len(path) >= k:
                t = path[-k:]
                if t == goal:
                    return True


            l = dfs(node.left, path)
            r = dfs(node.right, path)
            path.pop()

            return l or r

        return dfs(root, [])
            
        