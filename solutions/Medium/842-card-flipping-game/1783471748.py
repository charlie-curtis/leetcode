class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        H = set()
        bad = set()
        n = len(backs)
        for x,y in zip(fronts, backs):
            if x == y:
                bad.add(x)
            else:
                H.add(x)
                H.add(y)

        for x in sorted(H):
            if x not in bad:
                return x
        return 0
        