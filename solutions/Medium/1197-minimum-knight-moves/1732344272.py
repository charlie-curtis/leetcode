class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:


        q = deque()
        q.append((0,0,0))


        dirs = [
            [-2, -1],
            [-1, -2],
            [1, -2],
            [2, -1],
            [-2, 1],
            [-1, 2],
            [1, 2],
            [2,1]
        ]


        seen = set()
        while q:
            a,b, dst = q.popleft()

            if a == x and b == y:
                return dst

            for c,d in dirs:
                nxt_x = c+a
                nxt_y = d+b
                if (nxt_x, nxt_y) not in seen:
                    seen.add((nxt_x, nxt_y))
                    q.append((nxt_x, nxt_y, dst+1))

        