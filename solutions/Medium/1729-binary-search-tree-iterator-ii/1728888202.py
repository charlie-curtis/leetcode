# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    #to get next higher - if you have a right. then go rightt, then as far left as possible
    #if you don't have a right, then start popping parents until you find one where you're the left child

    #to get next lower
    #go left as far as possible
    #if you don't have a left, then while you have a parent and that parent isn't satisifed, pop it
    #basically, if you have a left, take it, but if not, then you have to be the right child of one of you parents somewhere down the line
    def __init__(self, root: Optional[TreeNode]):
        self.min = 1e10
        self.max = -1e10
        self.root = root
        self.stack = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.min = min(self.min, node.val)
            self.max = max(self.max, node.val)
            dfs(node.right)
        dfs(root)
        

    def hasNext(self) -> bool:
        return not self.stack or self.stack[-1].val != self.max

        

    def next(self) -> int:
        if not self.stack:
            self.stack.append(self.root)
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)
        elif self.stack[-1].right:
            self.stack.append(self.stack[-1].right)
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)
        else:
            cur = self.stack[-1].val
            print("I'm ", cur, "trying to get next")
            while self.stack[-1].val <= cur:
                self.stack.pop()
        print("NEXT ", self.stack[-1].val)
        return self.stack[-1].val

        

    def hasPrev(self) -> bool:
        return self.stack and self.stack[-1].val != self.min
        

    def prev(self) -> int:
        if self.stack[-1].left:
            self.stack.append(self.stack[-1].left)
            while self.stack[-1].right:
                self.stack.append(self.stack[-1].right)
        else:
            cur = self.stack[-1].val
            while self.stack[-1].val >= cur:
                self.stack.pop()
        print("PREV", self.stack[-1].val)
        return self.stack[-1].val
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()