class Trie:
    def __init__(self):
        self.root = {}
    
    def validate(self, path):
        if not path or path[0] != '/':
            return False
        parts = path.split('/')[1:]

        return all([len(x) > 0 for x in path.split('/')[1:]])

    def traverse(self, path, iscreate=False):
        parts = path.split('/')[1:]
        cur = self.root
        for i,x in enumerate(parts):
            if x not in cur:
                if i == len(parts)-1 and iscreate:
                    cur[x] = {}
                else:
                    return -1
            cur = cur[x]
        return cur

    def add(self, path, val):

        if not self.validate(path):
            return False
        
        cur = self.root
        t = self.traverse(path, True)
        if t == -1 or '_val_' in t:
            return False
        t['_val_'] = val
        return True

    def get(self, path):
        if not self.validate(path):
            return False

        t = self.traverse(path)
        if t == -1 or '_val_' not in t:
            return -1
        return t['_val_']
        
            
class FileSystem:

    def __init__(self):
        self.t = Trie()
        

    def createPath(self, path: str, value: int) -> bool:
        return self.t.add(path, value)
        

    def get(self, path: str) -> int:
        return self.t.get(path)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)