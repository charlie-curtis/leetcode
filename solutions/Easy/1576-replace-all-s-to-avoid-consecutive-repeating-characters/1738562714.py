class Solution:
    def modifyString(self, s: str) -> str:

        out = []
        n = len(s)
        for i,x in enumerate(s):
            if x == '?':
                avoid = set()
                if out:
                    avoid.add(out[-1])
                if i+1 < n:
                    avoid.add(s[i+1])

                for y in ['a', 'b', 'c']:
                    if y not in avoid:
                        out.append(y)
                        break
            else:
                out.append(x)

        return ''.join(out)
        