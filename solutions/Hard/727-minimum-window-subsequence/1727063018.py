class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        d = defaultdict(list)
        for i,x in enumerate(s1):
            d[x].append(i)

        positions = d[s2[0]]
        best = None
        for i in positions:
            j = i
            cur = 1
            while cur < len(s2):
                char = s2[cur]
                next_positions = d[char]
                idx = bisect_right(next_positions, j)
                if idx == len(next_positions):
                    break
                j = next_positions[idx]
                cur+=1
            if cur == len(s2):
                if not best or (abs(best[0] - best[1]) > abs(i-j)):
                    best = [i,j]
        return "" if not best else s1[best[0]:best[1]+1]



        