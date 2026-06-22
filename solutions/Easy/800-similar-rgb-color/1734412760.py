class Solution:
    def similarRGB(self, color: str) -> str:

        def to_int(c):
            return int(c, 16)
        def dst(a,b):
            return (a - b)**2
        
        out = ['', '', '']
        for j in range(3):
            best = 1e10
            c = color[1+2*j: 1+2*j+2]
            for i in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']:
                v = to_int(c)
                v2 = to_int(i)

                can = dst(v, v2)
                if can < best:
                    best = can
                    out[j] = i
        return '#' + ''.join(out)

