class Trie:
    def __init__(self):
        self.root = {}
    def add(self, word):
        node = self.root
        for x in word:
            if x not in node:
                node[x] = {}
            node = node[x]

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:

        t = Trie()
        for word in words:
            t.add(word)

        n = len(target)
        @cache
        def dp(i):
            if i == n:
                return 0
            
            best = float('inf')

            node = t.root
            for j in range(i,n):
                if target[j] in node:
                    best = min(best, 1 + dp(j+1))
                else:
                    break
                node = node[target[j]]
            return best
        res = dp(0)
        dp.cache_clear()
        return res if res < float('inf') else -1
        