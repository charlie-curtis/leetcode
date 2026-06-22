class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:

        hCuts.sort()
        vCuts.sort()
        hCuts = [0] + hCuts + [h]
        vCuts = [0] + vCuts + [w]

        MOD = 10**9 + 7

        x = 0
        for a,b in zip(vCuts, vCuts[1:]):
            x = max(x, b-a)
        y = 0
        for a,b in zip(hCuts, hCuts[1:]):
            y = max(y, b-a)
        return (x*y) % MOD