class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        d = defaultdict(int)
        for i,x in enumerate(keyboard):
            d[x] = i
        ans = 0
        for a,b in zip(keyboard[0] + word, word):
            ans+=abs(d[a] - d[b])
        return ans


        