class Trie:

    def __init__(self):
        self.root = {}
        self.root['_count_'] = 0
        

    def insert(self, word: str) -> None:

        tmp = self.root
        for x in word:
            tmp['_count_']+=1
            if x not in tmp:
                tmp[x] = {}
                tmp[x]['_count_'] = 0
            tmp = tmp[x]
        
        tmp['_count_']+=1
        if '_end_' not in tmp:
            tmp['_end_'] = 1
        else:
            tmp['_end_']+=1

    def countWordsEqualTo(self, word: str) -> int:
        tmp = self.root
        for x in word:
            if x not in tmp:
                return 0
            tmp = tmp[x]

        return 0 if '_end_' not in tmp else tmp['_end_']
        

    def countWordsStartingWith(self, word: str) -> int:
        tmp = self.root
        for x in word:
            if x not in tmp:
                return 0
            tmp = tmp[x]

        return tmp['_count_']
        

    def erase(self, word: str) -> None:
        tmp = self.root
        for x in word:
            tmp['_count_']-=1
            tmp = tmp[x]

        tmp['_count_']-=1
        tmp['_end_']-=1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)