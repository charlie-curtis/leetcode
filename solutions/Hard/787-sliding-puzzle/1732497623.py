class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        seen = set()
        q = deque()

        initial = ''.join([str(x) for x in board[0] + board[1]])
        target = '123450'
        neighbors = [
            [1,3],
            [0,2,4],
            [1,5],
            [0,4],
            [1,3,5],
            [2,4]
        ]


        def get_swap(b, idx, swap_idx):
            b = list(b)
            b[swap_idx],b[idx] = b[idx], b[swap_idx]
            return ''.join(b)

        def hydrate_moves(b):
            idx = b.find('0')
            for swap_idx in neighbors[idx]:
                tmp = get_swap(b, idx, swap_idx)
                if tmp not in seen:
                    q.append(tmp)
                    seen.add(tmp)

                
        moves = 0
        q.append(initial)
        while q:
            for _ in range(len(q)):
                b = q.popleft()
                if b == target:
                    return moves
                hydrate_moves(b)
            moves+=1

        return -1

            
        