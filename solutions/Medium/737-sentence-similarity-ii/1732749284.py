class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        d = defaultdict(set)
        for x in sentence1+sentence2:
            d[x].add(x)
        
        for a,b in similarPairs:
            d[a].add(b)
            d[b].add(a)


        def lookup(a,b, seen):
            if b in d[a]:
                return True
            if a in seen:
                return False
            else:
                seen.add(a)
                for nxt in d[a]:
                    if lookup(nxt,b, seen):
                        return True


        return all([lookup(a,b, set()) for a,b in list(zip(sentence1, sentence2))])
        