class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:


        def check(a,b,c,d):
            d1 = b[0] - a[0]
            d2 = d[0] - c[0]
            d3 = a[1] - c[1]
            d4 = b[1] - d[1]

            good = d1 == d2 == d3 == d4 and d1 > 0
            if not good:
                return False

            S = sqrt((a[0] - d[0])**2 + (a[1] - d[1])**2)
            T = sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
            return S == T


        for a,b,c,d in itertools.permutations([p1,p2,p3,p4]):
            if check(a,b,c,d):
                return True
        return False
        