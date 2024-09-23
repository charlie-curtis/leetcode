class Solution:
    def areSentencesSimilar(self, s1: List[str], s2: List[str], pairs: List[List[str]]) -> bool:

        d = defaultdict(set)
        for x,y in pairs:
            d[x].add(y)
            d[y].add(x)

        if len(s1) != len(s2):
            return False
        n = len(s1)
        for i in range(n):
            a = s1[i]
            b = s2[i]
            if a == b:
                continue
            if b not in d[a] or a not in d[b]:
                return False
        return True
        