class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:


        st = set()
        for x,y in points:
            st.add((x,y))

        def get_dst(A,B):
            return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
        def check(A,B,C):
            if A == B or A == C or B == C:
                return 0

            '''
            A --- B
            |     |
            |     |
            C --- D
            '''

            D = (C[0] + B[0] - A[0], C[1] + B[1] - A[1])
            if D not in st:
                return 0
            if list(D) in [A,B,C]:
                return 0
            d1 = get_dst(A,B)
            d2 = get_dst(D,C)

            d3 = get_dst(A,C)
            d4 = get_dst(B,D)

            T = get_dst(B,C)
            S = get_dst(A,D)

            if d1 != d2 or d3 != d4 or T != S:
                return 0

            return d1*d3 



        ans = 0
        for a in points:
            for b in points:
                if a == b:
                    continue
                for c in points:
                    if a == c or b == c:
                        continue
                    res = check(a,b,c)
                    if res > 0 and (ans == 0 or min(ans, res) == res):
                        ans = res
        return ans