class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self, word):
        special = '_cnt_'
        cur = self.root
        for x in word:
            kkey = str(len(word)) + word[-1] + x
            if kkey not in cur:
                cur[kkey] = {}
            cur = cur[kkey]
            if special not in cur:
                cur[special] = 0
            cur[special]+=1

    def getPref(self, word):
        special = '_cnt_'
        n = len(word)
        cur = self.root
        j = 0
        for i,x in enumerate(word):
            kkey = str(len(word)) + word[-1] + x
            cur = cur[kkey]
            if cur[special] == 1:
                j = i
                break
        if j == n-1:
            return word
        a = word[0:j+1]  + str((n-1-j-1)) + word[-1]
        if len(a) >= len(word):
            return word
        return a



class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:


        trie = Trie()
        for x in words:
            trie.add(x)
        out = []
        for x in words:
            out.append(trie.getPref(x))
        return out

        