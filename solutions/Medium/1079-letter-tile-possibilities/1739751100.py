class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        n = len(tiles)
        ans = set()
        A = [t for t in tiles]
        for l in range(1,n+1):
            for p in permutations(A, l):
                ans.add(p)
        return len(ans)