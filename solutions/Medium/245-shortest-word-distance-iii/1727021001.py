class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        lastSeen = {}
        ans = 1e10
        for i,x in enumerate(wordsDict):
            if x == word1 and word2 in lastSeen:
                ans = min(ans, i - lastSeen[word2])
            if x == word2 and word1 in lastSeen:
                ans = min(ans, i - lastSeen[word1])
            if x in [word1, word2]:
                lastSeen[x] = i
        return ans


        