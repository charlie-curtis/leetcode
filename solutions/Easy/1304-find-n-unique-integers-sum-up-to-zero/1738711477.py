class Solution:
    def sumZero(self, n: int) -> List[int]:
        pairs = n//2
        out = []
        for i in range(pairs):
            out.append(i+1)
            out.append(-i-1)
        
        if n % 2 == 1:
            out.append(0)
        return out
        