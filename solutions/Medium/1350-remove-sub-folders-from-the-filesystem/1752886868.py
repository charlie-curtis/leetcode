class Trie:

    def __init__(self):
        self.root = {}

    def insertAndCheck(self, word):

        tmp = self.root
        res = True
        for x in word:
            res&= '_end_' not in tmp
            if x not in tmp:
                tmp[x] = {}
            tmp = tmp[x]
        tmp['_end_'] = True
        return res
            


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder = sorted(folder, key=lambda x: len(x))
        out = []
        t = Trie()
        for x in folder:
            if t.insertAndCheck(x.split('/')):
                out.append(x)

        return out