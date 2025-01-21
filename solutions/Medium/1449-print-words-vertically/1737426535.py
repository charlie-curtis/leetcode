class Solution:
    def printVertically(self, tmp: str) -> List[str]:

        words = tmp.split()
        m = len(words)
        n = 0
        for x in words:
            n = max(n, len(x))
        out = defaultdict(list)

        for i in range(m):
            for j in range(n):
                out[j].append(words[i][j] if j < len(words[i]) else " ")
        real = []
        for i in sorted(out.keys()):
            r = ''.join(out[i]).rstrip()
            real.append(r)
        return real
        