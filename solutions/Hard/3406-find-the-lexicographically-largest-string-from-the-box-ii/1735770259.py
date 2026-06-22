class Solution:
    def answerString(self, word: str, n: int) -> str:

        if n == 1:
            return word

        m = len(word)
        other = n-1
        me = m-other

        options = []
        best = ""
        for i in range(m):
            end = min(m,i+me)
            w = word[i:end]
            best = max(best, w)

        return best
        