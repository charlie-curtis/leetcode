class Solution:
    def countBits(self, n: int) -> List[int]:

        go = lambda x: sum([int(y) for y in bin(x)[2:]]) 

        return [go(x) for x in range(0, n+1)]
        