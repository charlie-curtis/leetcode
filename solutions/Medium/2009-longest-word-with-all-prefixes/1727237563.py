class Trie():
    def __init__(self):
        self.next = {}

    def insert(self, word, i):
        if i == len(word):
            self.next["_end_"] = True
        else:
            letter = word[i]
            if letter not in self.next:
                self.next[letter] = Trie()
            self.next[letter].insert(word, i+1)
    
    def check(self, word, i):
        if i == len(word):
            return "_end_" in self.next

        letter = word[i]
        if letter not in self.next or "_end_" not in self.next:
            return False
        return self.next[letter].check(word,i+1)

class Solution:
    def longestWord(self, words: List[str]) -> str:

        t = Trie()
        words.append("")
        for x in words:
            t.insert(x, 0)

        candidates = [x for x in words if t.check(x,0)]
        def f(a,b):
            if len(a) != len(b):
                return a if len(a) > len(b) else b
            
            return a if a < b else b
        return reduce(f, candidates)