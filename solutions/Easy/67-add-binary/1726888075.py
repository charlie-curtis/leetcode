class Solution:
    def addBinary(self, a: str, b: str) -> str:

        n = max(len(a), len(b))

        out = []
        carry = 0
        for i in range(n):
            v1 = 0 if i >= len(a) else int(a[-i-1])
            v2 = 0 if i >= len(b) else int(b[-i-1])
            out.append((v1 + v2 + carry) % 2)
            carry = (v1+v2 + carry) // 2
        if carry:
            out.append(carry)
        ans = ''
        for x in out:
            ans = str(x) + '' + ans
        return ans