class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        out = []

        while a or b:
            canA = len(out) < 2 or ''.join(out[-2:]) != 'aa'
            canB = len(out) < 2 or ''.join(out[-2:]) != 'bb'
            if (a > b and canA) or not canB:
                a-=1
                out.append('a')
            else:
                out.append('b')
                b-=1
        return ''.join(out)

        