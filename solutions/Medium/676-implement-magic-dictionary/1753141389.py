class MagicDictionary:

    def __init__(self):
        self.d = defaultdict(set)

    def hashWord(self, word):
        n = len(word)
        return [word[0:i]+'*'+word[i+1:] for i in range(n)]
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for h in self.hashWord(word):
                self.d[h].add(word)

    def search(self, searchWord: str) -> bool:
        h = self.hashWord(searchWord)
        return any([(len(self.d[x]) == 1 and searchWord not in self.d[x]) or (len(self.d[x]) > 1) for x in h])
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)