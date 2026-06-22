class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        def check(a,b,c,d):

            if a[0] != c[0] or b[0] != d[0]:
                return 0
            if a[1] != b[1] or c[1] != d[1]:
                return 0

            return (a[1] - c[1])* (b[0] - a[0])



        d = defaultdict(list)
        for x,y in points:
            d[y].append(x)

        ans = 1e15
        hashes = defaultdict(set)
        for y,li in d.items():
            m = len(li)
            for i in range(m):
                for j in range(i+1,m):
                    x, x1 = li[i], li[j]
                    if x == x1:
                        continue
                    if x > x1:
                        x1,x = x, x1
                    for y1 in hashes[(x1,x)]:
                        ans = min(ans, (x1-x)*(abs(y1-y)))
                    hashes[(x1,x)].add(y)

        return ans if ans != 1e15 else 0
        