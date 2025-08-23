class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:

        cur = self.root
        for x in word:
            if x not in cur:
                cur[x] = {}
            cur = cur[x]
        cur['_end_'] = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for x in word:
            if x not in cur:
                return False
            cur = cur[x]
        return '_end_' in cur
        

    def startsWith(self, word: str) -> bool:
        cur = self.root
        for x in word:
            if x not in cur:
                return False
            cur = cur[x]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)