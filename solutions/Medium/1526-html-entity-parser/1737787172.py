class Solution:
    def entityParser(self, text: str) -> str:

        d = [s for s in text]
        d = d[::-1]

        mmap = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;' : '>',
            '&lt;' : '<',
            '&frasl;': '/'
        }

        out = []
        while d:
            m = len(d)
            for k,v in mmap.items():
                n = len(k)
                if len(d) >= n and ''.join(d[-n:]) == k[::-1]:
                    out.append(v)
                    for _ in range(n):
                        d.pop()
            if len(d) == m:
                out.append(d.pop())
        return ''.join(out)
        