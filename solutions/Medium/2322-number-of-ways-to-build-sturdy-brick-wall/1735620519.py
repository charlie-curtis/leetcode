class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:

        cans = []
        def generate(cur, ssum):
            nonlocal cans
            if ssum == width:
                cans.append(tuple(cur.copy()))
            elif ssum > width:
                return

            for x in bricks:
                cur.append(x)
                generate(cur, ssum + x)
                cur.pop()

        generate([], 0)

        @cache
        def getbreaks(a):
            return set(accumulate(a))
        
        @cache
        def iscompat(cur, prev):
            # Compute break points
            breaks_cur = getbreaks(cur)
            breaks_prev = getbreaks(prev)

            # Check if there is any overlap, except at the ends (0 and width)
            return breaks_cur.isdisjoint(breaks_prev - {0, width})


        d = defaultdict(set)
        n = len(cans)
        for i in range(n):
            for j in range(i,n):
                a,b = cans[i], cans[j]
                if iscompat(a,b):
                    d[a].add(b)
                    d[b].add(a)

        M = 10**9 + 7
        @cache
        def dp(i, prev):
            if i == height:
                return 1

            ans = 0
            avail = cans if not prev else d[prev]
            used = []
            for x in avail:
                used.append(x)
                a = dp(i+1, x)
                a%=M
                ans+=a
                ans%=M
            return ans

        return dp(0, ())