# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.cnt = self.dfs_count(root) 
        self.root = root

    def dfs_count(self,node):
        if not node:
            return 0
        R = self.dfs_count(node.right)
        L = self.dfs_count(node.left)
        return R + L + 1
        

    def getPath(self):
        v = self.cnt

        active = False
        path = []
        for i in range(15, -1, -1):
            hit = v&(1<<i)
            if not active:
                if hit:
                    active = True
                continue
            if hit:
                path.append('R')
            else:
                path.append('L')
        return path[::-1]
    def insert(self, val: int) -> int:
        self.cnt+=1
        if not self.root:
            self.root = TreeNode(val)
            return None
        p = self.getPath()
        print("path for ", self.cnt, "is", p)
        node = self.root
        while len(p):
            if p.pop() == 'L':
                if not p:
                    #we reached insertion
                    node.left = TreeNode(val)
                else:
                    #just traverse
                    node = node.left
            else:
                if not p:
                    #we reached insertion
                    node.right = TreeNode(val)
                else:
                    #just traverse
                    node = node.right
        return node.val


    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()