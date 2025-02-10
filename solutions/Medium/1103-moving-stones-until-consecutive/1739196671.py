class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        
        vals = sorted([a,b,c])
        low,mid,high=vals
        if low + 2 == mid+ 1 == high:
            return [0,0]
        if low+1 == mid or mid+1 ==  high or mid == low+2 or high == mid+2:
            return [1, high-low-2]
        return [2, high-low-2]
        