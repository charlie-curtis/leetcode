class Trie:
    def __init__(self):
        self.cnt = defaultdict(int) 
        self.nxt = defaultdict(Trie)
    
    def insert(self, word, i):
        self.cnt[i]+=1
        if i+1 < len(word):
            nxt_letter = word[i+1]
            self.nxt[nxt_letter].insert(word, i+1)

    def count(self, word, i):
        ans = self.cnt[i] if word[i] != "_" else 0
        if i+1 < len(word):
            nxt_letter = word[i+1]
            ans+=self.nxt[nxt_letter].count(word, i+1)
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        root = Trie()
        words = ["_" + w for w in words]
        for x in words:
            root.insert(x, 0)
        
        return [root.count(x, 0) for x in words]