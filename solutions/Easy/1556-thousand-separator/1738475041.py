class Solution:
    def thousandSeparator(self, n: int) -> str:


        out = []
        s = str(n)[::-1]
        m = len(s)
        for i in range(m):
            out.append(s[i])
            if (i+1) % 3 == 0 and i != m-1:
                out.append(".")

        ans = ''.join(out[::-1])
        return ans
