class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        def getMapping(s):
            n = len(s)
            sset = set([s])
            for i in range(n):
                s1 = s[:i] + '*' + s[i+1:]
                sset.add(s1)
                for j in range(i+1, n):
                    s2 = s1[:j] + '*' + s1[j+1:]
                    sset.add(s2)
            return sset

        sset = set()
        for s in dictionary:
            mapping = getMapping(s)
            sset.update(mapping)
        
        out = []
        for word in queries:
            for x in getMapping(word):
                if x in sset:
                    out.append(word)
                    break
        return out
