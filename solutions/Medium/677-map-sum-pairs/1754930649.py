class Trie:
    def __init__(self):
        self.root = {}
        self.seen  = {}
    
    def add(self, word, score):
        if word in self.seen:
            #adjust the score
            o = score
            score = score - self.seen[word]
            self.seen[word] = o
        else:
            self.seen[word] = score

        cur = self.root
        for x in word:
            if x not in cur:
                cur[x] = {}
            cur = cur[x]
            if '_score_' not in cur:
                cur['_score_'] = 0
            cur['_score_']+=score

    def getScore(self, word):
        cur = self.root
        for x in word:
            if x not in cur:
                return 0
            cur = cur[x]
        
        return cur['_score_']
            

class MapSum:

    def __init__(self):
        self.t = Trie()
        

    def insert(self, key: str, val: int) -> None:
        self.t.add(key, val)
        

    def sum(self, prefix: str) -> int:
        return self.t.getScore(prefix)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)