class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.words = defaultdict(set)
        for x in dictionary:
            ab = self.getAbbrev(x)
            self.words[ab].add(x)
        

    def isUnique(self, word: str) -> bool:
        ab = self.getAbbrev(word)
        sz = len(self.words[ab])
        exists = word in self.words[ab]
        return sz == 0 or (sz == 1 and exists)

    def getAbbrev(self, word):
        if len(word) == 2:
            return word
        
        return word[0] + str(len(word)-2) + word[-1]

    
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)