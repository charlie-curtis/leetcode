class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:

        #if a and b have matching bits, then we can keep both
        #if not, we can only enable the bit in one of the numbers, so choose the smaller

        #the reason we choose the smaller is because if a and b are as close as possible, they'll make the bigger product (e.g. 51*51 > 100*2)

        MOD = 10**9 + 7

        c = d = 0
        for i in range(n,64):
            c|=(1<<i)&a
            d|=(1<<i)&b
        for i in range(n-1,-1,-1):
            v = (1<<i)
            if a&v == b&v:
                #if bits match, we'll greedily choose an bit value for x that enables this bit in a and b
                c|=v
                d|=v
            elif c > d:
                d|=v
            else:
                c|=v
        return (c*d) % MOD

        