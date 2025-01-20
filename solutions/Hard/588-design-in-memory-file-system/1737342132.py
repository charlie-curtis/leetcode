class Trie:

    def __init__(self):
        self.root = {}
        self.root['_isFile_'] = False
        self.root['_contents_'] = ''
        self.root['_pq_'] = []
    
    def parsePath(self, path):
        out = []
        parts = path.split("/")

        for x in parts:
            if len(x) > 0:
                out.append(x)
        return out

    def add(self, path, isFile = False, contents = None):
        parts = self.parsePath(path)
        cur = self.root

        for p in parts:
            if p not in cur:
                cur[p] = {}
                cur[p]['_isFile_'] = False
                cur[p]['_contents_'] = ''
                cur[p]['_pq_'] = []
            cur = cur[p]
        
        cur['_isFile_'] = isFile
        if isFile:
            cur['_contents_']+= contents
    
    def get(self, path, justList):
        parts = self.parsePath(path)
        cur = self.root

        for p in parts:
            cur = cur[p]
        
        if justList:
            if cur['_isFile_']:
                return [parts[-1]]
            else:
                return sorted([x for x in cur.keys() if x not in ['_contents_', '_isFile_', '_pq_']])
        else:
            if not cur['_isFile_']:
                raise ValueError("Wrong")
            return cur['_contents_']


class FileSystem:

    def __init__(self):
        self.trie = Trie()
        

    def ls(self, path: str) -> List[str]:
        print("LS OF", path)
        return self.trie.get(path, True)
        

    def mkdir(self, path: str) -> None:
        print("MKDIR OF", path)
        return self.trie.add(path, False)
        

    def addContentToFile(self, path: str, content: str) -> None:
        print("Add File of", path)
        return self.trie.add(path, True, content)
        

    def readContentFromFile(self, path: str) -> str:
        print("Read File of", path)
        return self.trie.get(path, False)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


#r -> a -> b -> c -> d (isFile=boolean)


