class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)
        for i,x in enumerate(wordsDict):
            self.d[x].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:

        def get_distance(word, options):
            ans = 1e10
            for i in self.d[word]:
                idx = bisect.bisect_left(options, i)
                if idx != len(options):
                    ans = min(ans, abs(i-options[idx]))
            return ans
        
        a = get_distance(word1, self.d[word2])
        b = get_distance(word2, self.d[word1])

        return min(a,b)
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)