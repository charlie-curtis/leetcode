class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:

        groups = groupby(road)

        filtered = []
        for char, g in groups:
            if char != 'x': continue
            filtered.append(len(list(g)))

        filtered.sort(reverse=True)
        ans = 0
        for cnt in filtered:
            chosen = max(0,min(cnt, budget-1))
            ans+=chosen
            budget-=(chosen+1)
        return ans



        