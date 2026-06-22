class Solution:
    def minimumDistance(self, word: str) -> int:

        keyboard = ["ABCDEF", 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZ']
        d = defaultdict(int)
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                d[keyboard[i][j]] = (i,j)

        n = len(word)
        @cache
        def dp(h1, h2, i):
            if i == n:
                return 0

            x,y = d[word[i]]
            #use h1
            if h1[0] == -1 and h1[1] == -1:
                a = dp((x,y), h2, i+1)
            else:
                a = abs(x-h1[0]) + abs(y-h1[1]) + dp((x,y), h2, i+1)

            #use h2
            if h2[0] == -1 and h2[1] == -1:
                b = dp(h1, (x,y), i+1)
            else:
                b = abs(x-h2[0]) + abs(y-h2[1]) + dp(h1, (x,y), i+1)


            return min(a,b)
        return dp((-1,-1), (-1,-1), 0)