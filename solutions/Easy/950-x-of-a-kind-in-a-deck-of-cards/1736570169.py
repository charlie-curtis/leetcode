class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        C = Counter(deck)

        a = reduce(lambda x,y: math.gcd(x,y), C.values())
        return a > 1