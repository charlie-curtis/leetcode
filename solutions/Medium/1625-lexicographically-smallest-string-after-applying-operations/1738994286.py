class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:


        start = tuple([int(x) for x in s])
        q = [start]
        seen = set()
        seen.add(start)

        ans = start
        while q:

            cur = q.pop()
            if cur < ans:
                ans = cur

            ncur = []
            n = len(cur)
            #apply operation 1
            for i in range(n):
                x = cur[i]
                if i % 2 == 1:
                    ncur.append((x+a) % 10)
                else:
                    ncur.append(x)
            t = tuple(ncur)
            if t not in seen:
                seen.add(t)
                q.append(t)
            #apply operation 2
            ncur = list(cur)
            for i in range(n):
                ncur[(i+b)%n] = cur[i]

            t = tuple(ncur)
            if t not in seen:
                seen.add(t)
                q.append(t)
        #print(seen)
        return ''.join([str(x) for x in ans])