class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items.sort(key=lambda x: (x[0], -x[1]))

        li = []
        maxSeen = -1e10
        for p,b in items:
            maxSeen = max(maxSeen, b)
            if not li or li[-1][0] != p:
                li.append([p,maxSeen])
        out = []
        for p in queries:
            idx = bisect_right(li, p, key= lambda x: x[0]) - 1
            if idx == -1:
                out.append(0)
            else:
                out.append(li[idx][1])

        return out

        