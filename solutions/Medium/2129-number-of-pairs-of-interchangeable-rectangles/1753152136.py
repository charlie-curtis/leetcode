class Solution:
    def interchangeableRectangles(self, rect: List[List[int]]) -> int:

        C = Counter()
        for w,h in rect:
            g = gcd(w,h)
            w//=g
            h//=g
            C[(w,h)]+=1
        
        return sum([n*(n-1)//2 for n in C.values()])