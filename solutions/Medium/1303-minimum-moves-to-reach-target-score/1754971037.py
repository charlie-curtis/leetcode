class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        def do(x, cnt):
            if x == 1:
                return 0
            if cnt == 0:
                return x-1
            if x % 2 == 0:
                return do(x//2, cnt-1) + 1
            return do(x-1, cnt) + 1
        
        return do(target, maxDoubles)
        